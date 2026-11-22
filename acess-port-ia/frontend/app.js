(() => {
  const $ = (id) => document.getElementById(id);
  const STORAGE_KEY = "acess-port-ia-api-url";
  let apiBase = localStorage.getItem(STORAGE_KEY) || "http://127.0.0.1:8000";
  let refreshTimer = null;

  function updateClock() {
    const now = new Date();
    $("today").textContent = new Intl.DateTimeFormat("pt-BR", { dateStyle: "full" }).format(now);
    $("clock").textContent = now.toLocaleTimeString("pt-BR");
    $("eventDate").textContent = new Intl.DateTimeFormat("pt-BR", { dateStyle: "long" }).format(now);
  }

  function setApiState(connected, detail = "") {
    ["apiDot", "topApiDot"].forEach(id => {
      $(id).classList.toggle("green", connected);
      $(id).classList.toggle("muted", !connected);
    });
    $("apiStatus").textContent = connected ? "API conectada" : "API desconectada";
    $("topApiStatus").textContent = connected ? "API conectada" : "API desconectada";
    $("apiDetail").textContent = detail || (connected ? "Conectada" : "Não conectada");
  }

  function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, c => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
  }

  function renderCameras(cameras) {
    const grid = $("cameraGrid");
    if (!Array.isArray(cameras) || cameras.length === 0) {
      $("cameraSummary").textContent = "Nenhum canal retornado pela API";
      return;
    }

    grid.innerHTML = cameras.map((camera, index) => {
      const channel = Number(camera.canal ?? camera.channel ?? index + 1);
      const number = String(channel).padStart(2, "0");
      const online = String(camera.status || "").toUpperCase() === "ONLINE";
      const status = online ? "ONLINE" : "OFFLINE";
      const imageUrl = `${apiBase.replace(/\/$/, "")}/api/v1/cameras/${channel}/stream`;
      const source = escapeHtml(camera.source || "DVR");
      return `
        <article class="camera-card">
          <div class="camera-card-head">
            <span><i class="status-dot ${online ? "green" : "muted"}"></i> CÂMERA ${number}</span>
            <span class="camera-menu" title="Canal ${number}">•••</span>
          </div>
          <div class="camera-screen ${online ? "is-online" : "is-offline"}">
            ${online ? `<img src="${imageUrl}" alt="Transmissão da câmera ${number}" onerror="this.style.display='none';this.nextElementSibling.style.display='grid'">` : ""}
            <span class="stream-fallback" ${online ? 'style="display:none"' : ""}>${online ? "Falha ao carregar vídeo" : "Câmera offline"}</span>
            <span class="camera-overlay">CANAL ${number}</span>
          </div>
          <div class="camera-meta"><span>CANAL ${number} · ${source}</span><strong class="${online ? "online-text" : "offline-text"}">${status}</strong></div>
        </article>`;
    }).join("");

    const onlineCount = cameras.filter(c => String(c.status || "").toUpperCase() === "ONLINE").length;
    $("cameraSummary").textContent = `${onlineCount} de ${cameras.length} câmeras online`;
  }

  async function testApi() {
    setApiState(false, "Testando conexão...");
    try {
      const base = apiBase.replace(/\/$/, "");
      const healthResponse = await fetch(`${base}/api/v1/health`, { headers: { Accept: "application/json" } });
      if (!healthResponse.ok) throw new Error(`API respondeu HTTP ${healthResponse.status}`);
      const health = await healthResponse.json();
      const cameraResponse = await fetch(`${base}/api/v1/cameras`, { cache: "no-store" });
      if (!cameraResponse.ok) throw new Error(`Consulta de câmeras: HTTP ${cameraResponse.status}`);
      const payload = await cameraResponse.json();
      renderCameras(payload.cameras || payload.items || payload);
      setApiState(true, health.status || "Operacional");
      $("configFeedback").textContent = "Conexão realizada com sucesso.";
      $("configFeedback").className = "feedback success";
      return true;
    } catch (error) {
      setApiState(false, "Falha na conexão");
      $("cameraSummary").textContent = "Não foi possível consultar o DVR";
      $("configFeedback").textContent = `Não foi possível conectar: ${error.message}`;
      $("configFeedback").className = "feedback error";
      return false;
    }
  }

  function changeView(view) {
    const views = { camera: "cameraView", events: "eventsView", plates: "platesView" };
    Object.entries(views).forEach(([key, id]) => $(id).classList.toggle("hidden", key !== view));
    document.querySelectorAll(".nav-item[data-view]").forEach(button => button.classList.toggle("active", button.dataset.view === view));
    $("pageTitle").textContent = ({ camera: "Câmeras ao vivo", events: "Eventos de acesso", plates: "Placas e veículos" })[view];
    $("sidebar").classList.remove("open");
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
  $("apiForm").addEventListener("submit", async event => {
    event.preventDefault();
    const value = $("apiUrl").value.trim().replace(/\/$/, "");
    if (!/^https?:\/\//i.test(value)) {
      $("configFeedback").textContent = "Informe um endereço iniciado por http:// ou https://";
      $("configFeedback").className = "feedback error";
      return;
    }
    apiBase = value;
    localStorage.setItem(STORAGE_KEY, apiBase);
    const ok = await testApi();
    if (ok) $("apiDialog").close();
  });
  document.querySelectorAll(".nav-item[data-view]").forEach(button => {
    button.addEventListener("click", () => changeView(button.dataset.view));
  });
  $("menuToggle").addEventListener("click", () => $("sidebar").classList.toggle("open"));

  updateClock();
  setInterval(updateClock, 1000);
  testApi();
  refreshTimer = setInterval(testApi, 15000);
})();
