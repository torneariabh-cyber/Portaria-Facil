(() => {
  const $ = (id) => document.getElementById(id);
  const STORAGE_KEY = "acess-port-ia-api-url";
  let apiBase = localStorage.getItem(STORAGE_KEY) || "http://127.0.0.1:8000";

  function updateClock() {
    const now = new Date();
    $("today").textContent = new Intl.DateTimeFormat("pt-BR", { dateStyle: "full" }).format(now);
    $("clock").textContent = now.toLocaleTimeString("pt-BR");
    $("year").textContent = now.getFullYear();
  }

  function setApiState(connected, detail) {
    $("apiDot").classList.toggle("green", connected);
    $("apiDot").classList.toggle("muted", !connected);
    $("apiStatus").textContent = connected ? "API conectada" : "API desconectada";
    $("apiDetail").textContent = detail || (connected ? "Conectada" : "Não conectada");
    $("apiDetail").style.color = connected ? "#218154" : "";
  }

  function renderCameras(cameras) {
    const grid = $("cameraGrid");
    if (!Array.isArray(cameras) || !cameras.length) return;
    grid.innerHTML = cameras.slice(0, 4).map((camera, index) => {
      const online = camera.status === "online";
      const number = String(camera.channel ?? index + 1).padStart(2, "0");
      const status = online ? "ONLINE" : "AGUARDANDO CONEXÃO";
      const name = escapeHtml(camera.name || `Câmera ${number}`);
      const source = escapeHtml(camera.source || "DVR Intelbras");
      return `<article class="camera-card"><div class="camera-preview"><span class="camera-number">${number}</span><span class="camera-symbol">◉</span><span class="camera-pill">${status}</span></div><div class="camera-info"><strong>${name}</strong><small>Canal ${number} · ${source}</small></div></article>`;
    }).join("");
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  }

  async function testApi() {
    setApiState(false, "Testando...");
    try {
      const response = await fetch(`${apiBase.replace(/\/$/, "")}/api/v1/health`, { headers: { "Accept": "application/json" } });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const health = await response.json();
      setApiState(true, health.status === "ok" ? "Operacional" : "Conectada");
      const cameraResponse = await fetch(`${apiBase.replace(/\/$/, "")}/api/v1/cameras`);
      if (cameraResponse.ok) {
        const payload = await cameraResponse.json();
        renderCameras(payload.items || payload);
      }
      $("configFeedback").textContent = "Conexão realizada com sucesso.";
      $("configFeedback").className = "feedback success";
      return true;
    } catch (error) {
      setApiState(false, "Não conectada");
      $("configFeedback").textContent = `Não foi possível conectar: ${error.message}`;
      $("configFeedback").className = "feedback error";
      return false;
    }
  }

  $("settingsButton").addEventListener("click", () => {
    $("apiUrl").value = apiBase;
    $("configFeedback").textContent = "";
    $("apiDialog").showModal();
  });
  $("retryButton").addEventListener("click", testApi);
  $("apiForm").addEventListener("submit", async (event) => {
    if (event.submitter?.id !== "saveApi") return;
    event.preventDefault();
    const value = $("apiUrl").value.trim().replace(/\/$/, "");
    if (!/^https?:\/\//i.test(value)) {
      $("configFeedback").textContent = "Informe um endereço iniciado por http:// ou https://.";
      $("configFeedback").className = "feedback error";
      return;
    }
    apiBase = value;
    localStorage.setItem(STORAGE_KEY, apiBase);
    await testApi();
    if ($("apiDialog").open) $("apiDialog").close();
  });

  $("menuToggle").addEventListener("click", () => $("sidebar").classList.toggle("open"));
  document.querySelectorAll(".nav-item").forEach(link => link.addEventListener("click", () => $("sidebar").classList.remove("open")));

  updateClock();
  setInterval(updateClock, 1000);
  testApi();
})();
