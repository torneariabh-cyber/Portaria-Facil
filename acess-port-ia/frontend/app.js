(() => {
  const $ = (id) => document.getElementById(id);
  const STORAGE_KEY = "acess-port-ia-api-url";
  let apiBase = localStorage.getItem(STORAGE_KEY) || "http://127.0.0.1:8000";
  let cameraTimer = null;
  let eventTimer = null;
  let lastEventIds = new Set();

  const api = () => apiBase.replace(/\/$/, "");
  const esc = (v) => String(v ?? "—").replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));

  function updateClock() {
    const now = new Date();
    $("today").textContent = new Intl.DateTimeFormat("pt-BR", { dateStyle: "full" }).format(now);
    $("clock").textContent = now.toLocaleTimeString("pt-BR");
    $("eventDate").textContent = new Intl.DateTimeFormat("pt-BR", { dateStyle: "long" }).format(now);
  }

  function setApiState(ok, detail = "") {
    ["apiDot", "topApiDot"].forEach(id => {
      $(id).classList.toggle("green", ok);
      $(id).classList.toggle("muted", !ok);
    });
    $("apiStatus").textContent = ok ? "API conectada" : "API desconectada";
    $("topApiStatus").textContent = ok ? "API conectada" : "API desconectada";
    $("apiDetail").textContent = detail || (ok ? "Operacional" : "Não conectada");
  }

  function renderCameras(cameras) {
    const grid = $("cameraGrid");
    if (!Array.isArray(cameras) || !cameras.length) return;
    grid.innerHTML = cameras.map((camera, index) => {
      const channel = Number(camera.canal ?? camera.channel ?? index + 1);
      const number = String(channel).padStart(2, "0");
      const online = String(camera.status || "").toUpperCase() === "ONLINE";
      const stream = `${api()}/api/v1/cameras/${channel}/stream`;
      return `<article class="camera-card">
        <div class="camera-card-head"><span><i class="status-dot ${online ? "green" : "muted"}"></i> CÂMERA ${number}</span><span class="camera-menu">CANAL ${number}</span></div>
        <div class="camera-screen ${online ? "is-online" : "is-offline"}">
          ${online ? `<img src="${stream}" alt="Transmissão da câmera ${number}" onerror="this.style.display='none';this.nextElementSibling.style.display='grid'">` : ""}
          <span class="stream-fallback" ${online ? 'style="display:none"' : ""}>${online ? "Falha ao carregar vídeo" : "Câmera offline"}</span>
          <span class="camera-overlay">CANAL ${number}</span>
        </div>
        <div class="camera-meta"><span>CANAL ${number} · DVR</span><strong class="${online ? "online-text" : "offline-text"}">${online ? "ONLINE" : "OFFLINE"}</strong></div>
      </article>`;
    }).join("");
    const online = cameras.filter(c => String(c.status || "").toUpperCase() === "ONLINE").length;
    $("cameraSummary").textContent = `${online} de ${cameras.length} câmeras online`;
  }

  function dateParts(value) {
    if (!value) return { date: "—", time: "—" };
    const d = new Date(value);
    if (Number.isNaN(d.getTime())) return { date: esc(value), time: "" };
    return { date: d.toLocaleDateString("pt-BR"), time: d.toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit", second: "2-digit" }) };
  }

  function eventCard(event, compact = false) {
    const dt = dateParts(event.created_at);
    const imagePaths = Array.isArray(event.image_urls) && event.image_urls.length
      ? event.image_urls.slice(0, 4)
      : (event.image_url ? [event.image_url] : []);
    const dir = String(event.direction || "").toUpperCase();
    const isEntry = dir === "ENTRADA";
    const isExit = dir === "SAÍDA" || dir === "SAIDA";
    const directionClass = isEntry ? "entry" : "exit";
    const directionLabel = isEntry ? "ENTROU" : isExit ? "SAIU" : (dir || "SEM DIREÇÃO");
    const type = event.vehicle_type || "Não identificado";
    const color = event.color || "Não identificada";
    const photo = imagePaths.length
      ? `<div class="event-photo-grid count-${imagePaths.length}" aria-label="${imagePaths.length} fotos do veículo">${imagePaths.map((path, index) => `<img src="${esc(api() + path)}" alt="Foto ${index + 1} do veículo ${esc(event.plate || "sem placa")}" loading="lazy" onerror="this.classList.add('image-error')">`).join("")}</div>`
      : `<div class="event-photo-grid no-photo">SEM FOTO</div>`;
    return `<article class="event-card ${compact ? "compact" : ""}">
      ${photo}
      <div class="event-details">
        <div class="event-title-row"><strong class="event-plate">${esc(event.plate || "PLACA NÃO LIDA")}</strong><span class="direction-pill ${directionClass}">${esc(directionLabel)}</span></div>
        <div class="event-attributes"><span>${esc(type)}</span><span>Cor: ${esc(color)}</span><span>Câmera ${String(event.channel ?? "—").padStart(2, "0")}</span></div>
        <div class="event-time">${esc(dt.date)} · ${esc(dt.time)}</div>
      </div>
    </article>`;
  }

  function renderEvents(events) {
    const list = $("eventList");
    const valid = Array.isArray(events) ? events : [];
    // A lateral mostra somente os seis eventos mais recentes; o histórico completo permanece nas outras telas.
    list.innerHTML = valid.length
      ? valid.slice(0, 6).map(e => eventCard(e, true)).join("")
      : `<div class="event-empty"><span>◷</span><strong>Aguardando eventos</strong><small>Os veículos reconhecidos aparecerão aqui automaticamente.</small></div>`;

    const full = $("eventsFullList");
    if (full) {
      full.innerHTML = valid.length
        ? valid.map(e => eventCard(e, false)).join("")
        : `<div class="empty-panel"><span class="empty-icon">▤</span><strong>Nenhum evento recebido</strong><p>Os registros aparecerão aqui quando a IA identificar veículos.</p></div>`;
    }
    const plateList = $("platesFullList");
    if (plateList) {
      const withPlate = valid.filter(e => e.plate);
      plateList.innerHTML = withPlate.length
        ? withPlate.map(e => eventCard(e, false)).join("")
        : `<div class="empty-panel"><span class="empty-icon">▣</span><strong>Nenhuma placa reconhecida</strong><p>As placas identificadas serão listadas aqui.</p></div>`;
    }
    lastEventIds = new Set(valid.map(e => e.id));
  }

  async function refreshCameras() {
    try {
      const r = await fetch(`${api()}/api/v1/cameras`, { cache: "no-store" });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      const data = await r.json();
      renderCameras(data.cameras || data.items || data);
      setApiState(true, "Operacional");
      return true;
    } catch (err) {
      setApiState(false, "Falha na conexão");
      $("cameraSummary").textContent = `Não foi possível consultar as câmeras: ${err.message}`;
      return false;
    }
  }

  async function refreshEvents() {
    try {
      const r = await fetch(`${api()}/api/v1/events?limit=100`, { cache: "no-store" });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      const data = await r.json();
      renderEvents(data.events || []);
    } catch (err) {
      // Mantém o último histórico visível se houver falha momentânea.
      console.warn("Falha ao atualizar eventos:", err.message);
    }
  }

  async function testApi() {
    $("configFeedback").textContent = "Testando conexão...";
    try {
      const r = await fetch(`${api()}/api/v1/health`, { cache: "no-store" });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      const health = await r.json();
      setApiState(true, health.status || "Operacional");
      await Promise.all([refreshCameras(), refreshEvents()]);
      $("configFeedback").textContent = "Conexão realizada com sucesso.";
      $("configFeedback").className = "feedback success";
      return true;
    } catch (err) {
      setApiState(false, "Não conectada");
      $("configFeedback").textContent = `Não foi possível conectar: ${err.message}`;
      $("configFeedback").className = "feedback error";
      return false;
    }
  }

  function changeView(view) {
    const views = { camera: "cameraView", events: "eventsView", plates: "platesView" };
    Object.entries(views).forEach(([key, id]) => $(id).classList.toggle("hidden", key !== view));
    document.querySelectorAll(".nav-item[data-view]").forEach(b => b.classList.toggle("active", b.dataset.view === view));
    $("pageTitle").textContent = ({ camera: "Câmeras ao vivo", events: "Eventos de acesso", plates: "Placas e veículos" })[view];
    $("sidebar").classList.remove("open");
    if (view !== "camera") refreshEvents();
  }

  $("settingsButton").addEventListener("click", () => {
    $("apiUrl").value = apiBase;
    $("configFeedback").textContent = "";
    $("apiDialog").showModal();
  });
  $("closeDialog").addEventListener("click", () => $("apiDialog").close());
  $("cancelDialog").addEventListener("click", () => $("apiDialog").close());
  $("retryButton").addEventListener("click", testApi);
  $("railRetry").addEventListener("click", testApi);
  $("apiForm").addEventListener("submit", async e => {
    e.preventDefault();
    const value = $("apiUrl").value.trim().replace(/\/$/, "");
    if (!/^https?:\/\//i.test(value)) {
      $("configFeedback").textContent = "Informe um endereço iniciado por http:// ou https://";
      $("configFeedback").className = "feedback error";
      return;
    }
    apiBase = value;
    localStorage.setItem(STORAGE_KEY, apiBase);
    if (await testApi()) $("apiDialog").close();
  });
  document.querySelectorAll(".nav-item[data-view]").forEach(b => b.addEventListener("click", () => changeView(b.dataset.view)));
  $("menuToggle").addEventListener("click", () => $("sidebar").classList.toggle("open"));

  updateClock();
  setInterval(updateClock, 1000);
  testApi();
  cameraTimer = setInterval(refreshCameras, 15000);
  eventTimer = setInterval(refreshEvents, 4000);
})();
