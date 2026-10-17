
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Portaria Fácil — Prestadores de Serviço</title>
<style>
:root{--navy:#102b4e;--blue:#1768c4;--pale:#edf4fc;--ink:#172438;--muted:#66758b;--green:#12804a;--line:#dce4ee;--red:#b42318}
*{box-sizing:border-box}body{margin:0;background:#f2f5f9;color:var(--ink);font-family:Arial,Helvetica,sans-serif}
header{background:var(--navy);color:white;padding:18px 22px;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}.header-right{margin-left:auto;font-size:clamp(16px,2vw,22px);font-weight:700;font-variant-numeric:tabular-nums;white-space:nowrap}
body.display-mode header>div:first-child,body.display-mode header nav{display:none!important}body.display-mode header{position:fixed;top:0;right:0;z-index:20;background:transparent;padding:8px;pointer-events:none}body.display-mode .header-right{pointer-events:none;background:#dff5df;color:#14532d;border-radius:10px;width:max-content;height:auto;min-width:0;padding:8px 14px;display:flex;align-items:center;justify-content:center;font-size:clamp(18px,2vw,26px);line-height:1.2;box-shadow:0 2px 12px #0002}body.display-mode main{max-width:none;margin:0;padding:0}body.display-mode #displayView{display:block!important}body.display-mode #displayView .panel{margin:0;border:0;border-radius:0;box-shadow:none;min-height:100vh;width:100vw;padding:0;background:#000}body.display-mode #displayView .display-screen{position:relative;isolation:isolate;min-height:100vh;height:100vh;width:100vw;box-sizing:border-box;justify-content:center;padding:0;overflow:hidden;background:#fff!important;color:#172438}body.display-mode #displayView .display-screen:not(.showing-qr) #slideshow{width:100vw;height:100vh;max-width:none;max-height:none;margin:0 auto;border-radius:0;background:#000}
body.display-mode #displayView .display-screen.showing-qr #displayAddress{margin-top:7vh;position:relative;z-index:2;color:#172438} body.display-mode #displayView .display-screen.showing-qr .tag,body.display-mode #displayView .display-screen.showing-qr #qrOutput,body.display-mode #displayView .display-screen.showing-qr #countdown{position:relative;z-index:2} #displayBgLogo{display:none} body.display-mode .display-screen.showing-qr #displayBgLogo{display:block;position:absolute;inset:-18px;z-index:0;background-position:center;background-repeat:no-repeat;background-size:contain;filter:blur(5px);opacity:.12;pointer-events:none} body.display-mode .display-screen.showing-qr #qrOutput{background:#fff;border-radius:16px;box-shadow:0 4px 24px #0001}
body.display-mode #displayView .display-screen.showing-qr #qrOutput{width:15cm;height:12cm;min-width:0;min-height:0;margin:2vh auto 0;padding:0;border:0;display:flex;align-items:center;justify-content:center}
body.display-mode #displayView .display-screen.showing-qr #qrOutput img,body.display-mode #displayView .display-screen.showing-qr #qrOutput canvas{width:min(11cm,70vw)!important;height:auto!important;max-height:9cm}
body.display-mode #displayView .display-screen.showing-qr #countdown{width:max-content;max-width:90vw;height:auto;min-height:0;display:flex;align-items:center;justify-content:center;padding:8px 18px;margin:8px auto 0;font-size:clamp(28px,3.5vw,42px);line-height:1.1;background:#e4f7e2;color:#14532d;border:2px solid #b8e6b2;border-radius:12px;box-shadow:0 3px 12px #14532d12}
body.display-mode #displayView .display-screen.showing-qr #slideshow{display:none!important}body.display-mode #displayView .display-screen.showing-qr .tag{display:block!important}body.display-mode #displayView .display-screen.showing-qr #displayAddress{display:block!important}body.display-mode #displayView .display-screen.showing-qr #countdown[hidden]{display:none!important}
@media(max-width:700px){body.display-mode .header-right{width:auto;height:auto;padding:10px;font-size:18px}body.display-mode #displayView .display-screen.showing-qr #qrOutput,body.display-mode #displayView .display-screen.showing-qr #countdown{width:90vw;height:auto;min-height:0}body.display-mode #displayView .display-screen.showing-qr #countdown{padding:12px}}
header h1{font-size:clamp(20px,3vw,28px);margin:0}header p{margin:5px 0 0;color:#d7e5f7;font-size:14px}
nav{display:flex;gap:8px;flex-wrap:wrap}button,.button{border:0;border-radius:9px;padding:12px 15px;font-size:15px;font-weight:700;cursor:pointer}
nav button{background:#25476c;color:white}nav button.active{background:white;color:var(--navy)}
main{max-width:1100px;margin:22px auto;padding:0 14px 35px}.view{display:none}.view.active{display:block}
.panel{background:white;border:1px solid var(--line);border-radius:15px;padding:20px;box-shadow:0 4px 16px #18304b0a;margin-bottom:16px}
h2{font-size:20px;margin:0 0 15px}h3{margin:0 0 10px}
label{display:block;font-size:14px;font-weight:700;margin:12px 0 6px}
input,select,textarea{width:100%;border:1px solid #c8d3e1;border-radius:9px;padding:12px;font:inherit;background:#fff;color:var(--ink)}
textarea{min-height:160px;font-family:ui-monospace,Consolas,monospace;font-size:13px}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:15px}
.primary{background:var(--blue);color:white}.secondary{background:#e7eef7;color:#17385f}.green{background:var(--green);color:white}.danger{background:#fff0f0;color:var(--red)}
.hint{font-size:13px;color:var(--muted);line-height:1.5}.status{font-size:14px;min-height:20px;margin-top:10px;color:var(--green)}
.portaria-box{max-width:650px;margin:25px auto;text-align:center;padding:clamp(20px,5vw,42px)}
.portaria-box h2{font-size:clamp(24px,4vw,34px)}.portaria-box p{color:var(--muted)}
.bigbtn{width:100%;padding:18px;font-size:19px;margin-top:18px}
.display-screen{min-height:75vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.display-screen .tag{font-size:15px;text-transform:uppercase;letter-spacing:2px;color:var(--muted);font-weight:700}
.display-screen h2{font-size:clamp(30px,5vw,52px);margin:12px 0}
#qrOutput{background:white;padding:18px;border:1px solid var(--line);border-radius:16px;display:flex;align-items:center;justify-content:center;min-width:250px;min-height:250px;margin:18px auto}
#qrOutput img,#qrOutput canvas{max-width:min(65vw,360px);height:auto}
#countdown{font-size:clamp(22px,3vw,32px);font-weight:800;color:#14532d;background:#e4f7e2;border:2px solid #b8e6b2;border-radius:14px;padding:12px 22px;margin:0 0 14px;font-variant-numeric:tabular-nums;box-shadow:0 3px 12px #14532d12}
#slideshow{width:min(88vw,850px);height:min(58vh,520px);display:flex;align-items:center;justify-content:center;margin:18px auto;overflow:hidden;border-radius:16px}
#slideshow img,#slideshow video{display:block;max-width:100%;max-height:100%;width:100%;height:100%;object-fit:contain;background:#000}
#slideshow .empty{font-size:clamp(18px,3vw,28px);line-height:1.5;padding:25px}
#displayView .display-screen.showing-qr #slideshow{display:none}
#displayView .display-screen:not(.showing-qr) #qrOutput,#displayView .display-screen:not(.showing-qr) #countdown,#displayView .display-screen:not(.showing-qr) .tag,#displayView .display-screen:not(.showing-qr) #displayAddress{display:none}
#displayView .display-screen .actions,#displayView .display-screen .hint,#displayUrl{display:none!important}
#displayAddress .detail-line{display:block;margin:8px 0;font-size:clamp(22px,3vw,38px);font-weight:700}
#displayAddress .detail-label{font-weight:500;color:var(--muted);margin-right:8px}
#displayUrl{max-width:600px;overflow-wrap:anywhere;color:var(--muted);font-size:13px}
.table-wrap{overflow:auto}table{border-collapse:collapse;width:100%;min-width:570px}th,td{text-align:left;padding:11px;border-bottom:1px solid var(--line);font-size:14px}th{background:#f5f8fc}
.pill{display:inline-block;border-radius:999px;background:var(--pale);color:#174e8a;padding:5px 9px;font-size:12px;font-weight:bold}
.empty{text-align:center;color:var(--muted);padding:25px}
@media(max-width:650px){.grid{grid-template-columns:1fr}header{padding:16px}.panel{padding:15px}}
@media print{header,main>.view:not(#displayView),.no-print{display:none!important}body{background:white}main{margin:0;padding:0}.view#displayView{display:block!important}.panel{border:0;box-shadow:none}.display-screen{min-height:95vh}}

body.display-mode #floatingReportBtn{display:none!important}

/* Ajustes de compatibilidade visual para iPhone/Safari; preserva as funções existentes */
html { -webkit-text-size-adjust: 100%; }
body { padding-bottom: env(safe-area-inset-bottom); }
button, input, select, textarea { touch-action: manipulation; }
input, select, textarea { font-size: 16px; }
@supports (-webkit-touch-callout: none) {
  .view.active { -webkit-overflow-scrolling: touch; }
  body.display-mode #displayView .display-screen { min-height: 100svh; height: 100svh; padding-top: env(safe-area-inset-top); padding-bottom: env(safe-area-inset-bottom); }
  body.display-mode #floatingReportBtn { display: none !important; }
}
@media (max-width: 700px) {
  header { padding: 14px; }
  main { padding-left: 10px; padding-right: 10px; }
  .panel { padding: 14px; border-radius: 12px; }
  .grid { grid-template-columns: minmax(0, 1fr); }
  .actions > button, .actions > .button { flex: 1 1 100%; }
  nav { width: 100%; }
  nav button { flex: 1 1 auto; }
  body.display-mode #displayView .display-screen.showing-qr #qrOutput { width: 90vw; max-width: 90vw; height: auto; min-height: 0; margin-top: 2vh; padding: 8px; }
  body.display-mode #displayView .display-screen.showing-qr #qrOutput img,
  body.display-mode #displayView .display-screen.showing-qr #qrOutput canvas { width: min(72vw, 300px) !important; height: auto !important; max-height: 40svh; }
}

</style>
</head>
<body>
<header>
  <div><h1>Portaria Fácil <a href="https://maps.google.com/" target="_blank" rel="noopener noreferrer" title="Abrir Google Maps" aria-label="Abrir Google Maps" style="display:inline-flex;align-items:center;vertical-align:middle;margin-left:7px;text-decoration:none;font-size:25px">📍</a></h1><p>Localização rápida e inteligente Condominial</p></div>
  <div class="header-right" id="liveClock" aria-label="Hora atual">--:--:--</div>
  <nav class="no-print">
    <button class="active" data-view="portariaView">Portaria</button>
    <button data-view="displayView">Localização</button>
    <button data-view="cadastroView">Cadastrar links</button>
    <button class="secondary" id="openDisplayBtn">Abrir segunda tela</button>
  </nav>
</header>
<main>
<section id="portariaView" class="view active">
  <div class="panel portaria-box">
    <span class="pill">ACESSO RÁPIDO</span>
    <h2>Para qual imóvel é a entrega ou Serviço?</h2>
    <p>Selecione a rua/avenida ou a quadra e o lote. O QR Code será mostrado na tela de localização.</p>
    <div class="grid" style="text-align:left">
      <div><label for="ruaSelect">Rua / Avenida</label><select id="ruaSelect"><option value="">Todas as ruas e avenidas</option></select></div>
      <div><label for="quadraSelect">Quadra</label><select id="quadraSelect"><option value="">Selecione a quadra</option></select></div>
      <div><label for="loteSelect">Lote</label><select id="loteSelect" disabled><option value="">Selecione o lote</option></select></div>
      <div><label for="serviceTypeSelect">Tipo de Serviço</label><select id="serviceTypeSelect"><option value="">Selecione o tipo</option><option>Ifood</option><option>Mercado Livre</option><option>Shopee</option><option>TikTok Shop</option><option>Restaurante</option><option>Marmitaria</option><option>Serviços Gerais</option></select></div>
    </div>
    <button class="primary bigbtn" id="showBtn">MOSTRAR QR CODE</button>
    <div class="status" id="portariaStatus" role="status"></div>
  </div>
</section>

<section id="displayView" class="view">
  <div class="panel display-screen">
    <div id="displayBgLogo" aria-hidden="true"></div>
    <div class="tag">LOCALIZAÇÃO</div>
    <div id="slideshow" aria-label="Imagens do condomínio"><div class="empty">Bem-vindo ao Residencial Reserva Celeste 3</div></div>
    <h2 id="displayAddress">Aguardando seleção na portaria</h2>
    <div id="qrOutput"><div class="empty">Aguardando próxima localização.</div></div>
    <div id="countdown" aria-live="polite" hidden>02:00</div>
    <div id="displayUrl" hidden></div>
    <div class="actions no-print" style="justify-content:center">
      <button class="secondary" id="openMapBtn" disabled>Abrir mapa neste dispositivo</button>
      <button class="secondary" id="printQrBtn" disabled>Imprimir QR Code</button>
    </div>
    <p class="hint">O prestador de serviço pode escanear este QR Code com a câmera do celular para abrir a localização.</p>
  </div>
</section>

<section id="cadastroView" class="view">
  <div class="panel" id="loginPanel">
    <h2 id="authHeading">Acesso administrativo</h2>
    <p class="hint" id="authHint">Entre com o usuário e a senha para gerenciar os links e as imagens.</p>
    <div id="setupFields" hidden>
      <label for="setupUser">Criar usuário administrador</label><input id="setupUser" autocomplete="username" placeholder="Ex.: portaria.admin">
      <label for="setupPass">Criar senha</label><input id="setupPass" type="password" autocomplete="new-password" placeholder="Mínimo de 6 caracteres">
      <label for="setupRecovery">Código de recuperação (guarde em local seguro)</label><input id="setupRecovery" type="password" autocomplete="off" placeholder="Palavra ou código para recuperar a senha">
      <div class="actions"><button class="primary" id="createAuthBtn">Criar acesso</button></div>
    </div>
    <div id="loginFields">
      <label for="loginUser">Usuário</label><input id="loginUser" autocomplete="username" placeholder="Usuário">
      <label for="loginPass">Senha</label><input id="loginPass" type="password" autocomplete="current-password" placeholder="Senha">
      <div class="actions"><button class="primary" id="loginBtn">Entrar</button><button class="secondary" id="forgotPassBtn">Esqueci a senha</button></div>
    </div>
    <div id="recoverFields" hidden>
      <label for="recoverUser">Usuário</label><input id="recoverUser" autocomplete="username">
      <label for="recoverCode">Código de recuperação</label><input id="recoverCode" type="password" autocomplete="off">
      <label for="newPass">Nova senha</label><input id="newPass" type="password" autocomplete="new-password">
      <div class="actions"><button class="primary" id="resetPassBtn">Redefinir senha</button><button class="secondary" id="cancelRecoverBtn">Cancelar</button></div>
    </div>
    <div class="status" id="authStatus" role="status"></div>
  </div>
  <div id="adminContent" hidden>
    <div class="panel"><div class="actions" style="justify-content:flex-end;margin-top:0"><button class="secondary" id="changePassBtn">Trocar senha</button><button class="danger" id="logoutBtn">Sair</button></div></div>

  <div class="panel">
    <h2>Logo e imagens da tela de localização</h2>
    <label for="condoLogoFile">Logo de fundo para a tela do QR Code (opcional)</label>
    <input id="condoLogoFile" type="file" accept="image/*">
    <div class="actions"><button class="green" id="saveCondoLogoBtn">Salvar logo de fundo</button><button class="secondary" id="clearCondoLogoBtn">Remover logo</button></div>
    <p class="hint">Ao mostrar o QR Code, a tela fica branca e a logo aparece bem suave e desfocada ao fundo, sem atrapalhar a leitura do QR Code.</p>
    <p class="hint">Escolha até 3 imagens (logo do condomínio, avisos ou artes). Elas ficarão passando na segunda tela quando não houver QR Code. Ao gerar um QR Code, as imagens somem e voltam automaticamente quando os 2 minutos terminarem.</p>
    <label for="slideFiles">Selecionar logo/imagens (até 3)</label>
    <input id="slideFiles" type="file" accept="image/*" multiple>
    <div class="actions"><button class="green" id="saveSlidesBtn">Salvar imagens</button><button class="secondary" id="clearSlidesBtn">Remover imagens</button></div>
    <label for="videoFile">Selecionar um vídeo para a apresentação</label>
    <input id="videoFile" type="file" accept="video/mp4,video/webm,video/ogg">
    <p class="hint">O vídeo será alternado com as imagens a cada 10 segundos. Se houver somente vídeo ou somente imagens, esse conteúdo continuará sendo exibido sozinho. Para vídeos, prefira MP4 e arquivos de tamanho moderado.</p>
    <div class="actions"><button class="green" id="saveVideoBtn">Salvar vídeo</button><button class="secondary" id="clearVideoBtn">Remover vídeo</button></div>
    <div class="status" id="slideStatus" role="status"></div>
    <div id="slidePreviews" class="grid"></div>
  </div>
  <div class="panel">
    <h2>Importar todos os links de uma vez</h2>
    <p class="hint">Cole uma linha por imóvel no formato <b>Quadra;Lote;Link</b> (formato antigo) ou <b>Quadra;Lote;Rua/Avenida;Proprietário;Link</b>. Você também pode importar um arquivo CSV. O link deve ser o link compartilhável da localização alfinetada no mapa.</p>
    <label for="bulkInput">Lista de imóveis</label>
    <textarea id="bulkInput" placeholder="Quadra;Lote;Rua/Avenida;Proprietário;Link&#10;A;01;Avenida A;João da Silva;https://maps.google.com/...&#10;A;02;Rua 6;Maria Souza;https://maps.google.com/..."></textarea>
    <div class="actions">
      <button class="primary" id="importBtn">Importar lista</button>
      <button class="secondary" id="fileBtn">Escolher arquivo CSV</button>
      <input id="csvFile" type="file" accept=".csv,text/csv,text/plain" hidden>
      <button class="secondary" id="exportBtn">Exportar CSV</button>
      <button class="danger" id="clearBtn">Apagar todos</button>
    </div>
    <p class="hint">Linhas repetidas com a mesma quadra e lote atualizam o link existente. Cadastros ficam guardados neste navegador.</p>
    <div class="status" id="adminStatus" role="status"></div>
  </div>
  <div class="panel">
    <h2>Adicionar ou corrigir um imóvel</h2>
    <div class="grid">
      <div><label for="editQuadra">Quadra</label><input id="editQuadra" placeholder="Ex.: A"></div>
      <div><label for="editLote">Lote</label><input id="editLote" placeholder="Ex.: 01"></div>
      <div><label for="editRua">Rua / Avenida</label><input id="editRua" placeholder="Ex.: Avenida A, Rua 6"></div>
      <div><label for="editProprietario">Nome do proprietário</label><input id="editProprietario" placeholder="Nome completo"></div>
    </div>
    <label for="editUrl">Link da localização</label><input id="editUrl" type="url" placeholder="https://maps.google.com/...">
    <div class="actions"><button class="green" id="saveOneBtn">Salvar imóvel</button></div>
  </div>
  <div class="panel">
    <h2>Imóveis cadastrados <span class="pill" id="count">0 imóveis</span></h2>
    <div class="table-wrap"><table><thead><tr><th>Quadra</th><th>Lote</th><th>Rua / Avenida</th><th>Proprietário</th><th>Link</th><th>Ação</th></tr></thead><tbody id="recordsBody"><tr><td colspan="6" class="empty">Nenhum imóvel cadastrado.</td></tr></tbody></table></div>
  </div>
    <div class="panel" id="changePassPanel" hidden>
      <h2>Alterar senha</h2>
      <label for="currentPass">Senha atual</label><input id="currentPass" type="password" autocomplete="current-password">
      <label for="changeNewPass">Nova senha</label><input id="changeNewPass" type="password" autocomplete="new-password">
      <label for="changeRecovery">Código de recuperação atual</label><input id="changeRecovery" type="password" autocomplete="off">
      <div class="actions"><button class="primary" id="saveNewPassBtn">Salvar nova senha</button><button class="secondary" id="cancelChangePassBtn">Cancelar</button></div>
      <div class="status" id="changePassStatus" role="status"></div>
    </div>
  </div>
</section>
<section id="logsView" class="view">
  <div class="panel">
    <h2>Logs de navegação</h2>
    <p class="hint">Histórico armazenado somente neste navegador.</p>
    <div class="actions"><button class="secondary" id="exportLogsBtn">Exportar logs CSV</button><button class="danger" id="clearLogsBtn">Limpar logs</button></div><p class="hint">As entregas ficam registradas neste navegador. Clique no ícone de pasta no canto inferior direito para baixar o relatório CSV quando precisar.</p>
    <div class="table-wrap"><table><thead><tr><th>Data e hora</th><th>Ação</th><th>Detalhes</th></tr></thead><tbody id="logsBody"><tr><td colspan="3" class="empty">Nenhum registro.</td></tr></tbody></table></div>
  </div>
</section>
</main>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<script>
const STORAGE='portaria_facil_condominio_v2';
const CHANNEL='portaria_facil_condominio_sync_v2';
let records=[], current=null, expiryTimer=null, countdownInterval=null, slideInterval=null, slideImages=[], hasSlideVideo=false, slideVideoUrl=null, slideRenderToken=0;
const SLIDES_STORAGE='portaria_facil_condominio_slides_v1';
const VIDEO_META_STORAGE='portaria_facil_condominio_video_meta_v1';
const VIDEO_DB_NAME='portaria_facil_media_db_v1';
const VIDEO_STORE='media';
const CONDO_LOGO_STORAGE='portaria_facil_condominio_qr_logo_v1';
let condoLogo='';
try{condoLogo=localStorage.getItem(CONDO_LOGO_STORAGE)||''}catch(e){}
try{slideImages=JSON.parse(localStorage.getItem(SLIDES_STORAGE)||'[]')}catch(e){slideImages=[]}
try{hasSlideVideo=localStorage.getItem(VIDEO_META_STORAGE)==='1'}catch(e){hasSlideVideo=false}
function openMediaDb(){return new Promise((resolve,reject)=>{if(!('indexedDB' in window)){reject(new Error('Este navegador não oferece armazenamento de vídeo.'));return}const req=indexedDB.open(VIDEO_DB_NAME,1);req.onupgradeneeded=()=>{if(!req.result.objectStoreNames.contains(VIDEO_STORE))req.result.createObjectStore(VIDEO_STORE)};req.onsuccess=()=>resolve(req.result);req.onerror=()=>reject(req.error||new Error('Não foi possível abrir o armazenamento de mídia.'))})}
async function saveVideoBlob(file){const db=await openMediaDb();return new Promise((resolve,reject)=>{const tx=db.transaction(VIDEO_STORE,'readwrite');tx.objectStore(VIDEO_STORE).put(file,'presentation-video');tx.oncomplete=()=>{db.close();resolve()};tx.onerror=()=>{db.close();reject(tx.error||new Error('Falha ao salvar o vídeo.'))};tx.onabort=()=>{db.close();reject(tx.error||new Error('Falha ao salvar o vídeo.'))}})}
async function getVideoBlob(){const db=await openMediaDb();return new Promise((resolve,reject)=>{const tx=db.transaction(VIDEO_STORE,'readonly');const req=tx.objectStore(VIDEO_STORE).get('presentation-video');req.onsuccess=()=>{const result=req.result||null;db.close();resolve(result)};req.onerror=()=>{db.close();reject(req.error||new Error('Não foi possível ler o vídeo.'))}})}
async function deleteVideoBlob(){try{const db=await openMediaDb();await new Promise((resolve,reject)=>{const tx=db.transaction(VIDEO_STORE,'readwrite');tx.objectStore(VIDEO_STORE).delete('presentation-video');tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error);tx.onabort=()=>reject(tx.error)});db.close()}catch(e){}}
function broadcastMedia(){try{if('BroadcastChannel'in window){const c=new BroadcastChannel(CHANNEL);c.postMessage({type:'slides',images:slideImages,hasVideo:hasSlideVideo,logo:condoLogo});c.close()}}catch(e){}}
const LOG_STORAGE='portaria_facil_navigation_logs_v1';
const DELIVERY_STORAGE='portaria_facil_delivery_report_v1';
const DELIVERY_AUTODOWNLOAD_STORAGE='portaria_facil_delivery_report_last_auto_v1';
const DELIVERY_REPORT_INTERVAL=6*60*60*1000;
let deliveryEntries=[];try{deliveryEntries=JSON.parse(localStorage.getItem(DELIVERY_STORAGE)||'[]')}catch(e){deliveryEntries=[]}
function recordDelivery(r){
 const now=new Date();const entry={date:now.toLocaleDateString('pt-BR'),time:now.toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit',second:'2-digit'}),serviceType:$('serviceTypeSelect').value||'Não informado',quadra:r.quadra||'',lote:r.lote||'',rua:r.rua||'',proprietario:r.proprietario||'Não cadastrado'};
 deliveryEntries.push(entry);try{localStorage.setItem(DELIVERY_STORAGE,JSON.stringify(deliveryEntries))}catch(e){}
 logAction('Entrega/serviço registrado',`${entry.serviceType} — Quadra ${entry.quadra}, lote ${entry.lote}; morador: ${entry.proprietario}`);
}
function downloadDeliveryReport(auto=false){
 const headers=['Data','Hora','Tipo de serviço','Quadra','Lote','Rua/Avenida','Nome do proprietário/morador'];
 const rows=deliveryEntries.map(e=>[e.date,e.time,e.serviceType,e.quadra,e.lote,e.rua,e.proprietario]);
 const csv='\uFEFF'+[headers,...rows].map(row=>row.map(v=>'"'+String(v??'').replace(/"/g,'""')+'"').join(';')).join('\r\n');
 const blob=new Blob([csv],{type:'text/csv;charset=utf-8;'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download='relatorio_entregas_'+new Date().toISOString().slice(0,10)+'.csv';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
 if(auto)localStorage.setItem(DELIVERY_AUTODOWNLOAD_STORAGE,String(Date.now()));
}
function scheduleAutomaticDeliveryReport(){/* Registros mantidos internamente; o download ocorre somente ao clicar na pasta. */}

const $=id=>document.getElementById(id);
let logs=[];try{logs=JSON.parse(localStorage.getItem(LOG_STORAGE)||'[]')}catch(e){logs=[]}
function logAction(action,details=''){
  logs.unshift({date:new Date().toLocaleString('pt-BR'),action,details});
  logs=logs.slice(0,1000);
  try{localStorage.setItem(LOG_STORAGE,JSON.stringify(logs))}catch(e){}
  renderLogs();
}
function renderLogs(){
  const body=$('logsBody');if(!body)return;
  body.innerHTML=logs.length?logs.map(x=>`<tr><td>${escapeHtml(x.date)}</td><td>${escapeHtml(x.action)}</td><td>${escapeHtml(x.details||'')}</td></tr>`).join(''):'<tr><td colspan="3" class="empty">Nenhum registro.</td></tr>';
}
try{records=JSON.parse(localStorage.getItem(STORAGE)||'[]')}catch(e){records=[]}
function persist(){try{localStorage.setItem(STORAGE,JSON.stringify(records))}catch(e){};try{if('BroadcastChannel'in window){let c=new BroadcastChannel(CHANNEL);c.postMessage({type:'records',records});c.close()}}catch(e){}}
function validUrl(s){try{let u=new URL(s);return u.protocol==='https:'||u.protocol==='http:'}catch(e){return false}}
function key(q,l){return String(q).trim().toLocaleLowerCase()+'|'+String(l).trim().toLocaleLowerCase()}
function setStatus(id,msg,error=false){$(id).textContent=msg;$(id).style.color=error?'#b42318':'#12804a'}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
const AUTH_STORAGE='portaria_facil_admin_auth_v1';
let authData=null,adminAuthenticated=false;
try{authData=JSON.parse(localStorage.getItem(AUTH_STORAGE)||'null')}catch(e){authData=null}
function simpleHash(text){let h=2166136261;for(let i=0;i<text.length;i++){h^=text.charCodeAt(i);h=Math.imul(h,16777619)}return (h>>>0).toString(16)}
function isAdminAuthenticated(){return adminAuthenticated}
function showAuthPanel(){
 const firstSetup=!authData;
 $('loginPanel').hidden=false;$('adminContent').hidden=true;$('setupFields').hidden=!firstSetup;$('loginFields').hidden=firstSetup;$('recoverFields').hidden=true;
 $('authHeading').textContent=firstSetup?'Criar acesso administrativo':'Acesso administrativo';
 $('authHint').textContent=firstSetup?'No primeiro acesso, crie usuário, senha e um código de recuperação.':'Entre com seu usuário e senha para acessar os cadastros.';
}
function grantAdmin(){adminAuthenticated=true;$('loginPanel').hidden=true;$('adminContent').hidden=false;}
$('createAuthBtn').addEventListener('click',()=>{
 const username=$('setupUser').value.trim(),password=$('setupPass').value,recovery=$('setupRecovery').value;
 if(!username||password.length<6||recovery.length<4){setStatus('authStatus','Informe usuário, senha com pelo menos 6 caracteres e código de recuperação com pelo menos 4 caracteres.',true);return}
 authData={username:username.toLowerCase(),passwordHash:simpleHash(password),recoveryHash:simpleHash(recovery)};
 try{localStorage.setItem(AUTH_STORAGE,JSON.stringify(authData))}catch(e){}
 $('loginUser').value=username;$('loginPass').value='';showAuthPanel();setStatus('authStatus','Acesso criado. Entre com o usuário e a senha.',false);
});
$('loginBtn').addEventListener('click',()=>{
 const username=$('loginUser').value.trim().toLowerCase(),password=$('loginPass').value;
 if(authData&&username===authData.username&&simpleHash(password)===authData.passwordHash){grantAdmin();setStatus('adminStatus','Acesso administrativo autorizado.');logAction('Login administrativo','Acesso autorizado')}
 else setStatus('authStatus','Usuário ou senha incorretos.',true);
});
$('forgotPassBtn').addEventListener('click',()=>{$('loginFields').hidden=true;$('recoverFields').hidden=false;$('authStatus').textContent='';});
$('cancelRecoverBtn').addEventListener('click',()=>showAuthPanel());
$('resetPassBtn').addEventListener('click',()=>{
 const username=$('recoverUser').value.trim().toLowerCase(),code=$('recoverCode').value,newPass=$('newPass').value;
 if(!authData||username!==authData.username||simpleHash(code)!==authData.recoveryHash||newPass.length<6){setStatus('authStatus','Dados de recuperação inválidos ou senha menor que 6 caracteres.',true);return}
 authData.passwordHash=simpleHash(newPass);try{localStorage.setItem(AUTH_STORAGE,JSON.stringify(authData))}catch(e){};
 $('loginUser').value=username;$('loginPass').value='';showAuthPanel();setStatus('authStatus','Senha redefinida. Entre com a nova senha.',false);
});
$('logoutBtn').addEventListener('click',()=>{adminAuthenticated=false;$('changePassPanel').hidden=true;showAuthPanel();setStatus('authStatus','Você saiu do acesso administrativo.');});
$('changePassBtn').addEventListener('click',()=>{$('changePassPanel').hidden=!$('changePassPanel').hidden});
$('cancelChangePassBtn').addEventListener('click',()=>{$('changePassPanel').hidden=true});
$('saveNewPassBtn').addEventListener('click',()=>{
 const currentPass=$('currentPass').value,newPass=$('changeNewPass').value,recovery=$('changeRecovery').value;
 if(!authData||simpleHash(currentPass)!==authData.passwordHash||simpleHash(recovery)!==authData.recoveryHash||newPass.length<6){setStatus('changePassStatus','Confira a senha atual, o código de recuperação e use uma nova senha com pelo menos 6 caracteres.',true);return}
 authData.passwordHash=simpleHash(newPass);try{localStorage.setItem(AUTH_STORAGE,JSON.stringify(authData))}catch(e){};
 $('currentPass').value='';$('changeNewPass').value='';$('changeRecovery').value='';$('changePassPanel').hidden=true;setStatus('changePassStatus','Senha alterada com sucesso.');
});

function sortRecords(){records.sort((a,b)=>a.quadra.localeCompare(b.quadra,'pt-BR',{numeric:true})||a.lote.localeCompare(b.lote,'pt-BR',{numeric:true}))}
function renderSelectors(){
 const street=$('ruaSelect'),q=$('quadraSelect'),oldStreet=street.value,oldQ=q.value;
 const streets=[...new Set(records.map(r=>(r.rua||'').trim()).filter(Boolean))].sort((a,b)=>a.localeCompare(b,'pt-BR',{numeric:true}));
 street.innerHTML='<option value="">Todas as ruas e avenidas</option>'+streets.map(v=>`<option value="${escapeHtml(v)}">${escapeHtml(v)}</option>`).join('');
 if(streets.includes(oldStreet))street.value=oldStreet;
 const subset=records.filter(r=>!street.value||(r.rua||'').trim()===street.value);
 const qs=[...new Set(subset.map(r=>r.quadra))].sort((a,b)=>a.localeCompare(b,'pt-BR',{numeric:true}));
 q.innerHTML='<option value="">Selecione a quadra</option>'+qs.map(v=>`<option value="${escapeHtml(v)}">${escapeHtml(v)}</option>`).join('');
 if(qs.includes(oldQ))q.value=oldQ;
 renderLots();
}
function renderLots(){
 const street=$('ruaSelect').value,q=$('quadraSelect').value,l=$('loteSelect'),old=l.value;
 const ls=records.filter(r=>(!street||(r.rua||'').trim()===street)&&(!q||r.quadra===q)).sort((a,b)=>a.lote.localeCompare(b.lote,'pt-BR',{numeric:true}));
 l.innerHTML='<option value="">Selecione o lote</option>'+ls.map(r=>`<option value="${escapeHtml(r.lote)}">${escapeHtml(r.lote)}</option>`).join('');
 l.disabled=!q;if(ls.some(r=>r.lote===old))l.value=old;
}
function renderTable(){
 $('count').textContent=records.length+' imóvel(is)';
 $('recordsBody').innerHTML=records.length?records.map(r=>`<tr><td>${escapeHtml(r.quadra)}</td><td>${escapeHtml(r.lote)}</td><td>${escapeHtml(r.rua||'')}</td><td>${escapeHtml(r.proprietario||'')}</td><td><a href="${escapeHtml(r.url)}" target="_blank" rel="noopener">Abrir link</a></td><td><button class="secondary" data-edit="${escapeHtml(key(r.quadra,r.lote))}">Editar</button> <button class="danger" data-remove="${escapeHtml(key(r.quadra,r.lote))}">Excluir</button></td></tr>`).join(''):'<tr><td colspan="6" class="empty">Nenhum imóvel cadastrado.</td></tr>';
}
function renderAll(){sortRecords();renderSelectors();renderTable()}
function switchView(id){if(id==='cadastroView'&&!isAdminAuthenticated()){showAuthPanel();id='cadastroView'}document.querySelectorAll('.view').forEach(v=>v.classList.toggle('active',v.id===id));document.querySelectorAll('nav button').forEach(b=>b.classList.toggle('active',b.dataset.view===id));if(id==='displayView')renderCurrent();if(id==='logsView')renderLogs();logAction('Navegação',id)}
function findRecord(q,l){return records.find(r=>key(r.quadra,r.lote)===key(q,l))}
function scheduleExpiry(){
 if(expiryTimer)clearTimeout(expiryTimer);
 expiryTimer=null;
 if(!current)return;
 const expiresAt=Number(current._expiresAt)||Date.now()+120000;
 const delay=expiresAt-Date.now();
 if(delay<=0){showRecord(null);return;}
 expiryTimer=setTimeout(()=>{if(current&&Number(current._expiresAt)===expiresAt){showRecord(null);logAction('Localização expirada','QR Code e dados removidos após 2 minutos.')}},delay);
}
function showRecord(r){
 current=r?{...r,_expiresAt:Date.now()+120000}:null;
 try{if('BroadcastChannel'in window){let c=new BroadcastChannel(CHANNEL);c.postMessage({type:'current',record:current});c.close()}}catch(e){}
 renderCurrent();scheduleExpiry();
}
function updateClock(){
 const el=$('liveClock');if(el)el.textContent=new Date().toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit',second:'2-digit'});
}
function renderSlidePreviews(){
 const box=$('slidePreviews');if(!box)return;
 const imageCards=slideImages.map((src,i)=>`<div style="border:1px solid var(--line);border-radius:10px;padding:8px;text-align:center"><img src="${src}" alt="Imagem ${i+1}" style="max-width:100%;height:110px;object-fit:contain"><div class="hint">Imagem ${i+1}</div></div>`);
 if(hasSlideVideo)imageCards.push('<div style="border:1px solid var(--line);border-radius:10px;padding:18px;text-align:center"><strong>Vídeo salvo</strong><div class="hint">Será reproduzido na apresentação</div></div>');
 box.innerHTML=imageCards.join('');
}
async function renderSlideshow(){
 const box=$('slideshow');if(!box)return;
 if(slideInterval){clearInterval(slideInterval);slideInterval=null}
 const token=++slideRenderToken;
 if(slideVideoUrl){URL.revokeObjectURL(slideVideoUrl);slideVideoUrl=null}
 box.innerHTML='';
 if(current)return;
 let videoBlob=null;
 if(hasSlideVideo){try{videoBlob=await getVideoBlob()}catch(e){videoBlob=null}}
 if(token!==slideRenderToken||current)return;
 if(videoBlob)slideVideoUrl=URL.createObjectURL(videoBlob);
 const imageItems=slideImages.map(src=>({type:'image',src}));
 const items=[];
 // Quando existem imagens e vídeo, o vídeo toca até o fim e depois passa para as imagens.
 // Se não há imagens, o vídeo fica em repetição infinita.
 if(slideVideoUrl)items.push({type:'video',src:slideVideoUrl});
 items.push(...imageItems);
 if(!items.length){box.innerHTML='<div class="empty">Bem-vindo ao Residencial Reserva Celeste 3</div>';return}
 let index=0, imageTimer=null;
 const clearImageTimer=()=>{if(imageTimer){clearTimeout(imageTimer);imageTimer=null}};
 const showItem=()=>{
   clearImageTimer();
   if(current||token!==slideRenderToken)return;
   box.innerHTML='';const item=items[index];
   if(item.type==='image'){
     const img=document.createElement('img');img.alt='Imagem do condomínio';img.src=item.src;img.onerror=()=>{if(token===slideRenderToken){index=(index+1)%items.length;showItem()}};box.appendChild(img);
     if(items.length>1)imageTimer=setTimeout(()=>{if(current||token!==slideRenderToken)return;index=(index+1)%items.length;showItem()},10000);
   }else{
     const video=document.createElement('video');video.src=item.src;video.autoplay=true;video.muted=true;video.defaultMuted=true;video.loop=items.length===1;video.playsInline=true;video.preload='auto';
     video.setAttribute('playsinline','');video.setAttribute('muted','');video.setAttribute('autoplay','');if(items.length===1)video.setAttribute('loop','');
     video.style.width='100%';video.style.height='100%';video.style.objectFit='contain';
     video.addEventListener('ended',()=>{if(items.length>1&&token===slideRenderToken&&!current){index=(index+1)%items.length;showItem()}});
     video.addEventListener('error',()=>{if(token===slideRenderToken){box.innerHTML='<div class="empty">Não foi possível reproduzir este vídeo. Use MP4/H.264. Para maior compatibilidade, teste um vídeo curto e comprimido.</div>';if(items.length>1){imageTimer=setTimeout(()=>{index=(index+1)%items.length;showItem()},3000)}}});
     box.appendChild(video);
     const tryPlay=()=>{video.muted=true;video.defaultMuted=true;video.setAttribute('muted','');const p=video.play();if(p&&p.catch)p.catch(()=>{video.controls=true;video.setAttribute('controls','');});};
     video.addEventListener('loadedmetadata',tryPlay,{once:true});
     video.addEventListener('canplay',tryPlay,{once:true});
     tryPlay();
     box.addEventListener('click',()=>{video.muted=true;tryPlay()},{once:true});
   }
 };
 showItem();
}
function startCountdown(){
 if(countdownInterval)clearInterval(countdownInterval);
 const el=$('countdown');if(!current){el.hidden=true;return}
 el.hidden=false;
 const tick=()=>{const ms=Math.max(0,(Number(current?._expiresAt)||Date.now())-Date.now());const sec=Math.ceil(ms/1000);el.textContent=String(Math.floor(sec/60)).padStart(2,'0')+':'+String(sec%60).padStart(2,'0');if(sec<=0&&countdownInterval){clearInterval(countdownInterval);countdownInterval=null}};
 tick();countdownInterval=setInterval(tick,250);
}
async function imageToDataUrl(file){
 if(!file.type.startsWith('image/'))throw new Error('Selecione apenas arquivos de imagem.');
 const data=await new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result);reader.onerror=reject;reader.readAsDataURL(file)});
 const img=await new Promise((resolve,reject)=>{const im=new Image();im.onload=()=>resolve(im);im.onerror=reject;im.src=data});
 const scale=Math.min(1,1400/img.width,1000/img.height);const canvas=document.createElement('canvas');canvas.width=Math.max(1,Math.round(img.width*scale));canvas.height=Math.max(1,Math.round(img.height*scale));canvas.getContext('2d').drawImage(img,0,0,canvas.width,canvas.height);
 return canvas.toDataURL('image/jpeg',0.82);
}
$('saveCondoLogoBtn').addEventListener('click',async()=>{
 const file=$('condoLogoFile').files[0];if(!file){setStatus('slideStatus','Selecione uma imagem para usar como logo de fundo.',true);return}
 try{condoLogo=await imageToDataUrl(file);localStorage.setItem(CONDO_LOGO_STORAGE,condoLogo);const bg=$('displayBgLogo');if(bg)bg.style.backgroundImage=`url("${condoLogo}")`;broadcastMedia();setStatus('slideStatus','Logo de fundo salva com sucesso.');$('condoLogoFile').value=''}catch(e){setStatus('slideStatus','Não foi possível salvar a logo. Tente uma imagem menor.',true)}
});
$('clearCondoLogoBtn').addEventListener('click',()=>{condoLogo='';try{localStorage.removeItem(CONDO_LOGO_STORAGE)}catch(e){}const bg=$('displayBgLogo');if(bg)bg.style.backgroundImage='none';broadcastMedia();setStatus('slideStatus','Logo de fundo removida.')});
$('saveSlidesBtn').addEventListener('click',async()=>{
 const files=[...$('slideFiles').files];if(!files.length){setStatus('slideStatus','Selecione até 3 imagens antes de salvar.',true);return}
 if(files.length>3){setStatus('slideStatus','Selecione no máximo 3 imagens.',true);return}
 try{const converted=[];for(const f of files)converted.push(await imageToDataUrl(f));slideImages=converted;localStorage.setItem(SLIDES_STORAGE,JSON.stringify(slideImages));broadcastMedia();renderSlidePreviews();renderSlideshow();setStatus('slideStatus',`${slideImages.length} imagem(ns) salva(s).`);$('slideFiles').value=''}catch(e){setStatus('slideStatus','Não foi possível carregar as imagens. Tente arquivos menores.',true)}
});
$('clearSlidesBtn').addEventListener('click',()=>{slideImages=[];try{localStorage.removeItem(SLIDES_STORAGE)}catch(e){}broadcastMedia();renderSlidePreviews();renderSlideshow();setStatus('slideStatus','Imagens removidas.')});
$('saveVideoBtn').addEventListener('click',async()=>{
 const file=$('videoFile').files[0];if(!file){setStatus('slideStatus','Selecione um vídeo antes de salvar.',true);return}
 if(!file.type.startsWith('video/')){setStatus('slideStatus','Selecione um arquivo de vídeo válido.',true);return}
 try{await saveVideoBlob(file);hasSlideVideo=true;localStorage.setItem(VIDEO_META_STORAGE,'1');broadcastMedia();renderSlidePreviews();await renderSlideshow();setStatus('slideStatus','Vídeo salvo com sucesso.');$('videoFile').value=''}catch(e){setStatus('slideStatus','Não foi possível salvar o vídeo. Tente um arquivo menor ou outro navegador.',true)}
});
$('clearVideoBtn').addEventListener('click',async()=>{await deleteVideoBlob();hasSlideVideo=false;try{localStorage.removeItem(VIDEO_META_STORAGE)}catch(e){}broadcastMedia();renderSlidePreviews();renderSlideshow();setStatus('slideStatus','Vídeo removido.')});
function renderCurrent(){
 const screen=document.querySelector('#displayView .display-screen');
 const bgLogo=$('displayBgLogo');if(bgLogo)bgLogo.style.backgroundImage=condoLogo?`url("${condoLogo}")`:'none';
 if(screen)screen.classList.toggle('showing-qr',!!current);
 if(current){
  const details=[['Morador',current.proprietario||'Não cadastrado'],['Rua / Avenida',current.rua||'Não cadastrada'],['Quadra',current.quadra],['Lote',current.lote]];
  $('displayAddress').innerHTML=details.map(([label,value])=>`<span class="detail-line"><span class="detail-label">${escapeHtml(label)}:</span>${escapeHtml(value)}</span>`).join('');
 }else $('displayAddress').textContent='Aguardando seleção na portaria';
 $('displayUrl').textContent='';
 $('qrOutput').innerHTML='';
 startCountdown();
 if(!current)renderSlideshow();
 $('openMapBtn').disabled=!current;$('printQrBtn').disabled=!current;
 if(!current){$('qrOutput').innerHTML='<div class="empty">Aguardando próxima localização.</div>';return}
 // O QR Code fica vinculado ao link cadastrado deste imóvel.
 // O temporizador limpa apenas a tela; não altera o conteúdo do QR Code.
 const qrUrl=String(current.url||'').trim();
 if(!qrUrl){$('qrOutput').innerHTML='<div class="empty">Este imóvel não possui link cadastrado.</div>';return}
 let generated=false;
 if(window.QRCode){
  try{
   new QRCode($('qrOutput'),{text:qrUrl,width:300,height:300,colorDark:'#000000',colorLight:'#ffffff',correctLevel:QRCode.CorrectLevel?QRCode.CorrectLevel.H:3});
   generated=!!$('qrOutput').querySelector('canvas, img');
  }catch(err){generated=false;$('qrOutput').innerHTML=''}
 }
 // Alternativa caso a biblioteca principal não carregue.
 if(!generated){
  const img=document.createElement('img');
  img.alt='QR Code do link de localização cadastrado';img.width=300;img.height=300;
  img.style.width='300px';img.style.height='300px';img.style.maxWidth='min(65vw, 360px)';
  img.src='https://api.qrserver.com/v1/create-qr-code/?size=300x300&margin=10&data='+encodeURIComponent(qrUrl);
  img.onerror=()=>{$('qrOutput').innerHTML='<div class="empty">Não foi possível gerar o QR Code. Verifique a conexão com a internet e recarregue a página.</div>'};
  $('qrOutput').appendChild(img);
 }
}
$('ruaSelect').addEventListener('change',()=>{const street=$('ruaSelect').value;if($('quadraSelect').value&&!records.some(r=>r.quadra===$('quadraSelect').value&&(r.rua||'').trim()===street)&&street)$('quadraSelect').value='';$('loteSelect').value='';renderSelectors()});
$('quadraSelect').addEventListener('change',()=>{const q=$('quadraSelect').value,street=$('ruaSelect').value;if(street&&!records.some(r=>r.quadra===q&&(r.rua||'').trim()===street))$('ruaSelect').value='';$('loteSelect').value='';renderSelectors()});
$('loteSelect').addEventListener('change',()=>{const r=findRecord($('quadraSelect').value,$('loteSelect').value);if(r&&r.rua)$('ruaSelect').value=r.rua;renderSelectors();if(r)$('loteSelect').value=r.lote;});
$('showBtn').addEventListener('click',()=>{
 const q=$('quadraSelect').value,l=$('loteSelect').value;
 if(!q||!l){setStatus('portariaStatus','Selecione a quadra e o lote.',true);return}
 const r=findRecord(q,l);if(!r||($('ruaSelect').value&&(r.rua||'').trim()!==$('ruaSelect').value)){setStatus('portariaStatus','Imóvel não encontrado. Confira a rua/avenida, quadra e lote.',true);return}
 showRecord(r);recordDelivery(r);logAction('QR Code exibido',`Quadra ${r.quadra}, lote ${r.lote}`);setStatus('portariaStatus',`Exibindo QR Code: Quadra ${r.quadra}, Lote ${r.lote}.`);
});
$('openDisplayBtn').addEventListener('click',()=>{
 const w=window.open(location.href.split('#')[0]+'#tela-prestador','_blank');
 if(!w){setStatus('portariaStatus','O navegador bloqueou a segunda tela. Permita pop-ups para este arquivo.',true);return}
 try{const req=w.document.documentElement.requestFullscreen;if(req){const result=req.call(w.document.documentElement);if(result&&result.catch)result.catch(()=>{});}}catch(_){}
 setStatus('portariaStatus','Segunda tela aberta. O conteúdo se ajusta ao monitor; se o navegador não entrar em tela cheia automaticamente, pressione F11 nessa tela.');
});
$('openMapBtn').addEventListener('click',()=>{if(current)window.open(current.url,'_blank','noopener')});
$('printQrBtn').addEventListener('click',()=>window.print());
document.querySelectorAll('nav button[data-view]').forEach(b=>b.addEventListener('click',()=>switchView(b.dataset.view)));
function parseLine(line){
  let parts=line.split(';');
  if(parts.length<3)parts=line.split(',');
  if(parts.length<3)return null;
  const q=parts.shift().trim(),l=parts.shift().trim();
  let rua='',proprietario='',url='';
  if(parts.length===1){
    url=parts[0].trim().replace(/^["']|["']$/g,'');
  }else if(parts.length>=3){
    rua=parts.shift().trim().replace(/^["']|["']$/g,'');
    proprietario=parts.shift().trim().replace(/^["']|["']$/g,'');
    url=parts.join(line.includes(';')?';':',').trim().replace(/^["']|["']$/g,'');
  }else{
    url=parts.join(line.includes(';')?';':',').trim().replace(/^["']|["']$/g,'');
  }
  if(!q||!l||!validUrl(url))return null;
  return {quadra:q,lote:l,rua,proprietario,url};
}
function importText(text){
 const lines=text.replace(/^\uFEFF/,'').split(/\r?\n/).map(x=>x.trim()).filter(Boolean);
 let added=0,updated=0,skipped=0;
 lines.forEach((line,i)=>{
  if(i===0&&/quadra/i.test(line)&&/lote/i.test(line))return;
  const r=parseLine(line);if(!r){skipped++;return}
  const existing=findRecord(r.quadra,r.lote);
  if(existing){Object.assign(existing,r);updated++}else{records.push(r);added++}
 });
 persist();renderAll();logAction('Importação de imóveis',`${added} novos, ${updated} atualizados, ${skipped} ignorados`);setStatus('adminStatus',`Importação concluída: ${added} novo(s), ${updated} atualizado(s), ${skipped} linha(s) ignorada(s).`,false);
}
$('importBtn').addEventListener('click',()=>{if(!$('bulkInput').value.trim()){setStatus('adminStatus','Cole sua lista antes de importar.',true);return}importText($('bulkInput').value)});
$('fileBtn').addEventListener('click',()=>$('csvFile').click());
$('csvFile').addEventListener('change',async e=>{const f=e.target.files[0];if(f){importText(await f.text());e.target.value=''}});
$('saveOneBtn').addEventListener('click',()=>{
 const q=$('editQuadra').value.trim(),l=$('editLote').value.trim(),rua=$('editRua').value.trim(),proprietario=$('editProprietario').value.trim(),url=$('editUrl').value.trim();
 if(!q||!l||!validUrl(url)){setStatus('adminStatus','Preencha quadra, lote e um link http:// ou https:// válido.',true);return}
 const old=findRecord(q,l);if(old){Object.assign(old,{rua,proprietario,url})}else{records.push({quadra:q,lote:l,rua,proprietario,url})}
 persist();renderAll();logAction('Imóvel salvo',`Quadra ${q}, lote ${l}`);setStatus('adminStatus',`Quadra ${q}, lote ${l} salvo.`);
 $('editQuadra').value='';$('editLote').value='';$('editRua').value='';$('editProprietario').value='';$('editUrl').value='';
});
$('recordsBody').addEventListener('click',e=>{
 const ed=e.target.closest('[data-edit]'),rm=e.target.closest('[data-remove]');
 if(ed){const r=records.find(x=>key(x.quadra,x.lote)===ed.dataset.edit);if(r){$('editQuadra').value=r.quadra;$('editLote').value=r.lote;$('editRua').value=r.rua||'';$('editProprietario').value=r.proprietario||'';$('editUrl').value=r.url;window.scrollTo({top:0,behavior:'smooth'})}}
 if(rm){const r=records.find(x=>key(x.quadra,x.lote)===rm.dataset.remove);if(r&&confirm(`Excluir Quadra ${r.quadra}, Lote ${r.lote}?`)){records=records.filter(x=>x!==r);if(current&&key(current.quadra,current.lote)===key(r.quadra,r.lote))showRecord(null);persist();renderAll();logAction('Imóvel excluído',`Quadra ${r.quadra}, lote ${r.lote}`);setStatus('adminStatus','Imóvel excluído.')}} 
});
$('clearBtn').addEventListener('click',()=>{if(records.length&&confirm('Apagar todos os imóveis cadastrados neste navegador?')){records=[];showRecord(null);persist();renderAll();setStatus('adminStatus','Todos os cadastros foram apagados.')}});
$('exportBtn').addEventListener('click',()=>{
 const csv='\uFEFF'+[['Quadra','Lote','Rua/Avenida','Proprietário','Link'],...records.map(r=>[r.quadra,r.lote,r.rua||'',r.proprietario||'',r.url])].map(row=>row.map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(';')).join('\r\n');
 const blob=new Blob([csv],{type:'text/csv;charset=utf-8'}),a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='imoveis_condominio.csv';a.click();URL.revokeObjectURL(a.href);
});
window.addEventListener('storage',e=>{if(e.key===STORAGE){try{records=JSON.parse(e.newValue||'[]');renderAll()}catch(_){}}if(e.key===SLIDES_STORAGE){try{slideImages=JSON.parse(e.newValue||'[]');renderSlidePreviews();renderSlideshow()}catch(_){slideImages=[];renderSlideshow()}}if(e.key===VIDEO_META_STORAGE){hasSlideVideo=e.newValue==='1';renderSlidePreviews();renderSlideshow()}if(e.key===CONDO_LOGO_STORAGE){condoLogo=e.newValue||'';const bg=$('displayBgLogo');if(bg)bg.style.backgroundImage=condoLogo?`url("${condoLogo}")`:'none'}});
if('BroadcastChannel'in window){const channel=new BroadcastChannel(CHANNEL);channel.onmessage=e=>{if(e.data?.type==='records'){records=e.data.records||[];renderAll()}if(e.data?.type==='current'){current=e.data.record||null;renderCurrent();scheduleExpiry()}if(e.data?.type==='slides'){slideImages=e.data.images||[];if(typeof e.data.hasVideo==='boolean')hasSlideVideo=e.data.hasVideo;if(typeof e.data.logo==='string'){condoLogo=e.data.logo;try{localStorage.setItem(CONDO_LOGO_STORAGE,condoLogo)}catch(_){}const bg=$('displayBgLogo');if(bg)bg.style.backgroundImage=condoLogo?`url("${condoLogo}")`:'none'};try{localStorage.setItem(SLIDES_STORAGE,JSON.stringify(slideImages));if(hasSlideVideo)localStorage.setItem(VIDEO_META_STORAGE,'1');else localStorage.removeItem(VIDEO_META_STORAGE)}catch(_){}renderSlidePreviews();renderSlideshow()}}}
if(location.hash==='#tela-prestador'){document.body.classList.add('display-mode');switchView('displayView');}


renderAll();renderSlidePreviews();renderSlideshow();renderCurrent();updateClock();setInterval(updateClock,1000);showAuthPanel();
</script>
<button id="floatingReportBtn" type="button" title="Baixar relatório de entregas" aria-label="Baixar relatório de entregas" style="position:fixed;right:18px;bottom:18px;z-index:9999;width:58px;height:50px;border:1px solid #d6b64b;border-radius:12px;background:#fff4bd;color:#243247;box-shadow:0 4px 14px #0003;font-size:29px;display:flex;align-items:center;justify-content:center;cursor:pointer">📂</button>
<script>
(function(){
  const btn = document.getElementById('floatingReportBtn');
  if (btn) btn.addEventListener('click', function(){
    if (typeof downloadDeliveryReport === 'function') downloadDeliveryReport(false);
  });
})();
</script>
</body>
</html>
