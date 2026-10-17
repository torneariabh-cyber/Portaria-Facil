<html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Portaria Fácil — Prestadores de Serviço</title>
<style>
:root{--navy:#102b4e;--blue:#1768c4;--pale:#edf4fc;--ink:#172438;--muted:#66758b;--green:#12804a;--line:#dce4ee;--red:#b42318;--gold:#f0b429}
*{box-sizing:border-box}body{margin:0;background:#f2f5f9;color:var(--ink);font-family:Arial,Helvetica,sans-serif;-webkit-font-smoothing:antialiased}
header{background:linear-gradient(135deg,#0d2340,#102b4e 40%,#1a3f6b);color:white;padding:16px 22px;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;box-shadow:0 2px 16px #0002}.header-right{margin-left:auto;display:flex;align-items:center;gap:10px;font-size:clamp(15px,2vw,20px);font-weight:700;font-variant-numeric:tabular-nums;white-space:nowrap}
.cloud-pill{display:inline-flex;align-items:center;gap:6px;padding:6px 12px;border-radius:999px;font-size:12px;font-weight:700;background:#e4f7e2;color:#14532d;box-shadow:0 2px 8px #0002;cursor:help}
.cloud-pill.err{background:#ffe0de;color:#b42318}
.cloud-pill.load{background:#fff3c4;color:#92600a}

body.display-mode header>div:first-child,body.display-mode header nav,body.display-mode .cloud-pill{display:none!important}body.display-mode header{position:fixed;top:0;right:0;z-index:20;background:transparent;padding:8px;pointer-events:none}body.display-mode .header-right{pointer-events:none;background:#dff5df;color:#14532d;border-radius:10px;width:max-content;height:auto;min-width:0;padding:8px 14px;display:flex;align-items:center;justify-content:center;font-size:clamp(18px,2vw,26px);line-height:1.2;box-shadow:0 2px 12px #0002}body.display-mode main{max-width:none;margin:0;padding:0}body.display-mode #displayView{display:block!important}body.display-mode #displayView .panel{margin:0;border:0;border-radius:0;box-shadow:none;min-height:100vh;width:100vw;padding:0;background:#000}body.display-mode #displayView .display-screen{position:relative;isolation:isolate;min-height:100vh;height:100vh;width:100vw;box-sizing:border-box;justify-content:center;padding:0;overflow:hidden;background:#fff!important;color:#172438}body.display-mode #displayView .display-screen:not(.showing-qr) #slideshow{width:100vw;height:100vh;max-width:none;max-height:none;margin:0 auto;border-radius:0;background:#000}
body.display-mode #displayView .display-screen.showing-qr #displayAddress{margin-top:7vh;position:relative;z-index:2;color:#172438} body.display-mode #displayView .display-screen.showing-qr .tag,body.display-mode #displayView .display-screen.showing-qr #qrOutput,body.display-mode #displayView .display-screen.showing-qr #countdown{position:relative;z-index:2} #displayBgLogo{display:none} body.display-mode .display-screen.showing-qr #displayBgLogo{display:block;position:absolute;inset:-18px;z-index:0;background-position:center;background-repeat:no-repeat;background-size:contain;filter:blur(5px);opacity:.12;pointer-events:none} body.display-mode .display-screen.showing-qr #qrOutput{background:#fff;border-radius:16px;box-shadow:0 4px 24px #0001}
body.display-mode #displayView .display-screen.showing-qr #qrOutput{width:15cm;height:12cm;min-width:0;min-height:0;margin:2vh auto 0;padding:0;border:0;display:flex;align-items:center;justify-content:center}
body.display-mode #displayView .display-screen.showing-qr #qrOutput img,body.display-mode #displayView .display-screen.showing-qr #qrOutput canvas{width:min(11cm,70vw)!important;height:auto!important;max-height:9cm}
body.display-mode #displayView .display-screen.showing-qr #countdown{width:max-content;max-width:90vw;height:auto;min-height:0;display:flex;align-items:center;justify-content:center;padding:8px 18px;margin:8px auto 0;font-size:clamp(28px,3.5vw,42px);line-height:1.1;background:#e4f7e2;color:#14532d;border:2px solid #b8e6b2;border-radius:12px;box-shadow:0 3px 12px #14532d12}
body.display-mode #displayView .display-screen.showing-qr #slideshow{display:none!important}body.display-mode #displayView .display-screen.showing-qr .tag{display:block!important}body.display-mode #displayView .display-screen.showing-qr #displayAddress{display:block!important}body.display-mode #displayView .display-screen.showing-qr #countdown[hidden]{display:none!important}
@media(max-width:700px){body.display-mode .header-right{width:auto;height:auto;padding:10px;font-size:18px}body.display-mode #displayView .display-screen.showing-qr #qrOutput,body.display-mode #displayView .display-screen.showing-qr #countdown{width:90vw;height:auto;min-height:0}body.display-mode #displayView .display-screen.showing-qr #countdown{padding:12px}}
header h1{font-size:clamp(20px,3vw,26px);margin:0;letter-spacing:-.5px}header p{margin:4px 0 0;color:#a9c5e6;font-size:13px}
nav{display:flex;gap:8px;flex-wrap:wrap;align-items:center}button,.button{border:0;border-radius:12px;padding:12px 18px;font-size:14px;font-weight:700;cursor:pointer;transition:all .18s ease;font-family:inherit;letter-spacing:.2px;box-shadow:0 2px 6px #0001}
nav button{background:linear-gradient(135deg,#1e3a5c,#25476c);color:white;border:1px solid #ffffff15}nav button:hover{background:linear-gradient(135deg,#25476c,#2d5580);transform:translateY(-1px);box-shadow:0 4px 10px #0003}nav button.active{background:linear-gradient(135deg,#ffffff,#f0f6ff);color:var(--navy);box-shadow:0 4px 12px #0003}
main{max-width:1100px;margin:22px auto;padding:0 14px 35px}.view{display:none}.view.active{display:block;animation:fadeIn .3s ease}@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.panel{background:white;border:1px solid var(--line);border-radius:18px;padding:22px;box-shadow:0 6px 24px #18304b0e;margin-bottom:16px}
h2{font-size:20px;margin:0 0 15px;color:var(--navy)}h3{margin:0 0 10px;color:var(--navy)}
label{display:block;font-size:13px;font-weight:700;margin:14px 0 6px;color:var(--ink);text-transform:uppercase;letter-spacing:.5px}
input,select,textarea{width:100%;border:2px solid #d9e2ee;border-radius:12px;padding:13px;font:inherit;background:#fafcff;color:var(--ink);transition:all .18s ease}input:focus,select:focus,textarea:focus{outline:none;border-color:var(--blue);background:#fff;box-shadow:0 0 0 4px #1768c415}
textarea{min-height:160px;font-family:ui-monospace,Consolas,monospace;font-size:13px}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px;justify-content:center}
.primary{background:linear-gradient(135deg,#1768c4,#0e56a8);color:white;box-shadow:0 4px 14px #1768c450}.primary:hover{background:linear-gradient(135deg,#1e78d8,#105ec0);transform:translateY(-2px);box-shadow:0 8px 20px #1768c460}
.secondary{background:linear-gradient(135deg,#eef4fb,#dde8f5);color:#17385f;border:1px solid #c8d8ea}.secondary:hover{background:linear-gradient(135deg,#e2ecf8,#cddcf0);transform:translateY(-1px)}
.green{background:linear-gradient(135deg,#12804a,#0c6338);color:white;box-shadow:0 4px 14px #12804a40}.green:hover{background:linear-gradient(135deg,#169955,#0e7342);transform:translateY(-2px);box-shadow:0 8px 20px #12804a50}
.danger{background:linear-gradient(135deg,#fff0f0,#ffe0e0);color:var(--red);border:1px solid #ffc9c9}.danger:hover{background:linear-gradient(135deg,#ffe5e5,#ffd0d0)}
.hint{font-size:13px;color:var(--muted);line-height:1.5}.status{font-size:14px;min-height:20px;margin-top:10px;color:var(--green);font-weight:600}
.portaria-box{max-width:650px;margin:25px auto;text-align:center;padding:clamp(24px,5vw,48px)}
.portaria-box h2{font-size:clamp(24px,4vw,32px);margin-bottom:8px}.portaria-box p{color:var(--muted);margin-top:0;margin-bottom:22px}
.pill{display:inline-block;border-radius:999px;background:linear-gradient(135deg,#edf4fc,#d9e8fa);color:#174e8a;padding:6px 14px;font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;box-shadow:0 2px 6px #174e8a20}
.bigbtn{width:100%;padding:20px;font-size:18px;margin-top:24px;border-radius:14px;letter-spacing:.5px}
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
.table-wrap{overflow:auto;border-radius:12px;border:1px solid var(--line)}table{border-collapse:collapse;width:100%;min-width:570px}th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);font-size:14px}th{background:linear-gradient(135deg,#f5f8fc,#eef4fb);font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:.5px;font-size:12px}
tr:hover td{background:#fafcff}
.empty{text-align:center;color:var(--muted);padding:25px}
@media(max-width:650px){.grid{grid-template-columns:1fr}header{padding:14px}header h1{font-size:18px}.panel{padding:16px;border-radius:14px}nav button{padding:10px 14px;font-size:13px}}
@media print{header,main>.view:not(#displayView),.no-print{display:none!important}body{background:white}main{margin:0;padding:0}.view#displayView{display:block!important}.panel{border:0;box-shadow:none}.display-screen{min-height:95vh}}

body.display-mode #floatingReportBtn{display:none!important}

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
  .panel { padding: 16px; }
  .grid { grid-template-columns: minmax(0, 1fr); }
  .actions > button, .actions > .button { flex: 1 1 100%; }
  nav { width: 100%; justify-content: center; }
  nav button { flex: 1 1 auto; }
  body.display-mode #displayView .display-screen.showing-qr #qrOutput { width: 90vw; max-width: 90vw; height: auto; min-height: 0; margin-top: 2vh; padding: 8px; }
  body.display-mode #displayView .display-screen.showing-qr #qrOutput img,
  body.display-mode #displayView .display-screen.showing-qr #qrOutput canvas { width: min(72vw, 300px) !important; height: auto !important; max-height: 40svh; }
}

/* ========== Página de navegação ========== */
.nav-page{max-width:560px;margin:0 auto;padding:18px 14px 40px;font-family:Arial,Helvetica,sans-serif}
.nav-page .nav-header{background:linear-gradient(135deg,#0d2340,#102b4e 50%,#1a3f6b);color:#fff;border-radius:20px;padding:22px;text-align:center;margin-bottom:16px;box-shadow:0 8px 24px #102b4e30}
.nav-page .nav-header .tag{font-size:12px;text-transform:uppercase;letter-spacing:3px;color:#a9c5e6;font-weight:800}
.nav-page .nav-header h1{font-size:clamp(22px,5vw,28px);margin:10px 0 0;line-height:1.25}
.nav-page .card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;margin-bottom:14px;box-shadow:0 4px 16px #18304b0a}
.nav-page .info-line{display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-bottom:1px dashed var(--line);font-size:15px}
.nav-page .info-line:last-child{border-bottom:0}
.nav-page .info-line .lbl{color:var(--muted);font-weight:700}
.nav-page .info-line .val{color:var(--ink);font-weight:700;text-align:right;word-break:break-word}
.nav-page .big-link{display:flex;align-items:center;gap:14px;width:100%;padding:18px;border-radius:14px;border:2px solid var(--line);background:#fff;text-decoration:none;color:var(--ink);font-weight:700;font-size:16px;margin-bottom:10px;cursor:pointer;transition:all .15s ease;box-shadow:0 2px 8px #18304b0a}
.nav-page .big-link:active{transform:scale(.98)}
.nav-page .big-link .ico{font-size:28px;line-height:1;width:38px;text-align:center;flex-shrink:0}
.nav-page .big-link .txt{flex:1;text-align:left}
.nav-page .big-link .txt small{display:block;color:var(--muted);font-weight:400;font-size:13px;margin-top:2px}
.nav-page .big-link.gmaps{background:linear-gradient(135deg,#e8f1fe,#d7e8ff);border-color:#1768c4}
.nav-page .big-link.waze{background:linear-gradient(135deg,#e6f6ff,#d0eaff);border-color:#00a8e8}
.nav-page .big-link.apple{background:linear-gradient(135deg,#f0f0f5,#e0e0e8);border-color:#888}
.nav-page .big-link.copy{background:linear-gradient(135deg,#fff8e1,#fff3c4);border-color:#d4a017}
.nav-page .big-link.orig{background:linear-gradient(135deg,#e8f7ee,#d7f0e0);border-color:#12804a}
.nav-page .notice{font-size:13px;color:var(--muted);text-align:center;margin-top:14px}
.nav-page .copy-feedback{color:var(--green);font-size:13px;margin-top:6px;text-align:center;min-height:18px;font-weight:600}

/* ========== Totem do portão ========== */
.totem-page{max-width:520px;margin:0 auto;padding:18px 14px 40px;font-family:Arial,Helvetica,sans-serif;display:flex;flex-direction:column;min-height:100vh;min-height:100svh;box-sizing:border-box}
.totem-page .totem-header{background:linear-gradient(135deg,#0d2340,#102b4e 40%,#1a3f6b);color:#fff;border-radius:20px;padding:26px 20px;text-align:center;margin-bottom:18px;box-shadow:0 10px 28px #102b4e40;position:relative;overflow:hidden}
.totem-page .totem-header::before{content:'';position:absolute;top:-40%;right:-30%;width:200px;height:200px;background:radial-gradient(circle,#1768c440 0%,transparent 70%);pointer-events:none}
.totem-page .totem-header .tag{font-size:11px;text-transform:uppercase;letter-spacing:4px;color:#a9c5e6;font-weight:800}
.totem-page .totem-header h1{font-size:clamp(22px,6vw,28px);margin:12px 0 6px;line-height:1.2;position:relative;z-index:1}
.totem-page .totem-header p{margin:6px 0 0;color:#d7e5f7;font-size:14px;line-height:1.4;position:relative;z-index:1}
.totem-page .card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;margin-bottom:14px;box-shadow:0 6px 24px #18304b0e}
.totem-page .card h3{margin:0 0 4px;font-size:17px;color:var(--navy)}
.totem-page .card .sub{color:var(--muted);font-size:13px;margin-bottom:16px}
.totem-page label{display:block;font-size:12px;font-weight:800;margin:16px 0 6px;color:var(--ink);text-transform:uppercase;letter-spacing:.6px}
.totem-page select{width:100%;border:2px solid #d9e2ee;border-radius:12px;padding:15px;font-size:16px;font-weight:600;background:#fafcff;color:var(--ink);-webkit-appearance:none;appearance:none;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%2366758b' stroke-width='3'><path d='M6 9l6 6 6-6'/></svg>");background-repeat:no-repeat;background-position:right 16px center;padding-right:44px;transition:all .18s ease}
.totem-page select:focus{outline:none;border-color:var(--blue);background:#fff;box-shadow:0 0 0 4px #1768c418}
.totem-page select:disabled{background:#f2f5f9;color:#a7b1c0;cursor:not-allowed}
.totem-page .bigbtn{width:100%;padding:22px;font-size:19px;font-weight:800;border:0;border-radius:14px;background:linear-gradient(135deg,#12804a,#0c6338);color:#fff;cursor:pointer;margin-top:22px;box-shadow:0 10px 26px #12804a45;letter-spacing:.6px;transition:all .15s ease;text-transform:uppercase}
.totem-page .bigbtn:hover:not(:disabled){background:linear-gradient(135deg,#169955,#0e7342);transform:translateY(-2px);box-shadow:0 14px 32px #12804a55}
.totem-page .bigbtn:active:not(:disabled){transform:scale(.98)}
.totem-page .bigbtn:disabled{background:linear-gradient(135deg,#d0d8e3,#b8c4d4);color:#7d8896;box-shadow:none;cursor:not-allowed}
.totem-page .status{font-size:14px;min-height:20px;margin-top:12px;color:var(--red);text-align:center;font-weight:600}
.totem-page .footer-area{margin-top:auto;padding-top:24px;text-align:center}
.totem-page .speed-badge{display:inline-flex;align-items:center;gap:10px;padding:14px 22px;border-radius:14px;background:linear-gradient(135deg,#fff3c4,#ffe58f);color:#6a4c00;font-weight:800;font-size:15px;box-shadow:0 4px 14px #d4a01730;margin-top:16px;letter-spacing:.5px}
.totem-page .speed-badge .ico{font-size:22px}
.totem-page .speed-badge .val{font-size:22px;color:#92600a}

.totem-result{max-width:520px;margin:0 auto;padding:18px 14px 40px;font-family:Arial,Helvetica,sans-serif}
.totem-result .result-card{background:#fff;border:1px solid var(--line);border-radius:20px;padding:24px;box-shadow:0 8px 28px #18304b12;margin-bottom:14px}
.totem-result .result-header{text-align:center;margin-bottom:20px}
.totem-result .result-header .tag{font-size:11px;text-transform:uppercase;letter-spacing:3px;color:var(--muted);font-weight:800}
.totem-result .result-header h2{font-size:clamp(24px,6vw,32px);margin:10px 0 6px;color:var(--navy);line-height:1.15}
.totem-result .result-header .addr{color:var(--muted);font-size:15px;line-height:1.4}
.totem-result .result-header .proprietario{color:var(--ink);font-size:16px;font-weight:700;margin-top:6px}
.totem-result .nav-buttons{display:flex;flex-direction:column;gap:12px;margin-top:8px}
.totem-result .nav-btn{display:flex;align-items:center;gap:16px;width:100%;padding:20px;border-radius:16px;border:2px solid var(--line);background:#fff;text-decoration:none;color:var(--ink);font-weight:800;font-size:18px;cursor:pointer;box-shadow:0 4px 14px #18304b0e;text-align:left;transition:all .15s ease}
.totem-result .nav-btn:hover{transform:translateY(-2px);box-shadow:0 8px 22px #18304b18}
.totem-result .nav-btn:active{transform:scale(.98)}
.totem-result .nav-btn .ico{font-size:32px;line-height:1;width:44px;text-align:center;flex-shrink:0}
.totem-result .nav-btn .txt{flex:1}
.totem-result .nav-btn .txt small{display:block;color:var(--muted);font-weight:500;font-size:12px;margin-top:3px;text-transform:uppercase;letter-spacing:.5px}
.totem-result .nav-btn.gmaps{background:linear-gradient(135deg,#e8f1fe,#d7e8ff);border-color:#1768c4;color:#0d3f7c}
.totem-result .nav-btn.waze{background:linear-gradient(135deg,#e6f6ff,#d0eaff);border-color:#00a8e8;color:#005f8a}
.totem-result .nav-btn.apple{background:linear-gradient(135deg,#f0f0f5,#e0e0e8);border-color:#666;color:#222}
.totem-result .nav-btn.copy{background:linear-gradient(135deg,#fff8e1,#fff3c4);border-color:#d4a017;color:#6a4c00}
.totem-result .nav-btn.copy .ico{font-size:26px}
.totem-result .speed-warn{display:flex;align-items:center;justify-content:center;gap:10px;padding:14px;border-radius:12px;background:linear-gradient(135deg,#fff3c4,#ffe58f);color:#6a4c00;font-weight:800;font-size:14px;margin-top:18px;text-align:center}
.totem-result .speed-warn .ico{font-size:22px}
.totem-result .backbtn{width:100%;padding:16px;font-size:15px;font-weight:700;border:0;border-radius:12px;background:linear-gradient(135deg,#eef4fb,#dde8f5);color:#17385f;cursor:pointer;margin-top:10px;transition:all .15s ease}
.totem-result .backbtn:hover{background:linear-gradient(135deg,#e2ecf8,#cddcf0)}
.totem-result .feedback{color:var(--green);font-size:14px;text-align:center;min-height:20px;margin-top:6px;font-weight:600}

.qr-portao-preview{background:#fff;padding:24px;border:2px solid var(--line);border-radius:20px;display:inline-flex;align-items:center;justify-content:center;min-width:260px;min-height:260px;margin:14px 0;box-shadow:0 8px 24px #18304b10}
.qr-portao-preview img,.qr-portao-preview canvas{max-width:280px!important;height:auto!important}

/* Modal de login do admin (totem) */
.modal-overlay{position:fixed;inset:0;background:#0d2340dd;z-index:9999;display:none;align-items:center;justify-content:center;padding:18px;backdrop-filter:blur(4px)}
.modal-overlay.active{display:flex;animation:fadeIn .2s ease}
.modal-card{background:#fff;border-radius:20px;padding:26px;max-width:400px;width:100%;box-shadow:0 20px 60px #0005;animation:slideUp .25s ease}
@keyframes slideUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}
.modal-card h3{margin:0 0 6px;font-size:20px;color:var(--navy)}
.modal-card .sub{color:var(--muted);font-size:13px;margin-bottom:18px}
.modal-card label{margin-top:14px}
.modal-card input{background:#fafcff}
.modal-card .actions{margin-top:20px}
.modal-card .error{color:var(--red);font-size:13px;min-height:18px;margin-top:8px;text-align:center;font-weight:600}

.speed-card{background:linear-gradient(135deg,#fff8e1,#fff3c4);border:2px solid #f0d570;border-radius:16px;padding:18px;margin-bottom:16px;display:flex;align-items:center;gap:16px;box-shadow:0 4px 14px #d4a01720}
.speed-card .ico{font-size:36px}
.speed-card .txt{flex:1}
.speed-card .txt strong{display:block;font-size:14px;color:#6a4c00;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px}
.speed-card .txt span{font-size:22px;font-weight:800;color:#92600a}
</style>
</head>
<body>

<div id="navPage" style="display:none">
  <div class="nav-page">
    <div class="nav-header">
      <div class="tag">LOCALIZAÇÃO DO IMÓVEL</div>
      <h1 id="navTitle">Residencial Reserva Celeste 3</h1>
      <div class="sub" id="navSub">Escolha como deseja abrir a rota</div>
    </div>
    <div class="card">
      <div class="info-line"><span class="lbl">Proprietário</span><span class="val" id="navProprietario">—</span></div>
      <div class="info-line"><span class="lbl">Rua / Avenida</span><span class="val" id="navRua">—</span></div>
      <div class="info-line"><span class="lbl">Quadra</span><span class="val" id="navQuadra">—</span></div>
      <div class="info-line"><span class="lbl">Lote</span><span class="val" id="navLote">—</span></div>
      <div class="info-line"><span class="lbl">Tipo de serviço</span><span class="val" id="navService">—</span></div>
    </div>
    <div class="card">
      <h3 style="margin:0 0 12px;font-size:16px;color:var(--navy)">Abrir rota em:</h3>
      <a class="big-link gmaps" id="navGmaps" href="#" target="_blank" rel="noopener"><span class="ico">🗺️</span><span class="txt">Google Maps<small>Navegação padrão</small></span></a>
      <a class="big-link waze" id="navWaze" href="#" target="_blank" rel="noopener"><span class="ico">🚗</span><span class="txt">Waze<small>Trânsito em tempo real</small></span></a>
      <a class="big-link apple" id="navApple" href="#" target="_blank" rel="noopener"><span class="ico">🍎</span><span class="txt">Apple Maps<small>iPhone / iPad</small></span></a>
      <a class="big-link orig" id="navOriginal" href="#" target="_blank" rel="noopener"><span class="ico">🌐</span><span class="txt">Abrir link original</span></a>
      <button class="big-link copy" id="navCopyBtn" type="button"><span class="ico">📋</span><span class="txt">Copiar endereço<small id="navCopyPreview">—</small></span></button>
      <div class="copy-feedback" id="navCopyFeedback"></div>
    </div>
  </div>
</div>

<div id="totemPage" style="display:none">
  <div class="totem-page" id="totemForm">
    <div class="totem-header">
      <div class="tag">BEM-VINDO</div>
      <h1>Residencial Reserva Celeste III</h1>
      <p>Selecione o imóvel e abra a localização direto no seu GPS.</p>
    </div>
    <div class="card">
      <h3>📍 PARA ONDE VOCÊ VAI?</h3>
      <div class="sub">Escolha a Rua, Quadra e o Lote do Morador.</div>
      <div id="totemLoading" class="hint" style="text-align:center;padding:20px">⏳ Carregando imóveis...</div>
      <div id="totemFormFields" style="display:none">
        <label for="totemRua">RUA / Avenida</label>
        <select id="totemRua"><option value="">Todas as ruas e avenidas</option></select>
        <label for="totemQuadra">QUADRA</label>
        <select id="totemQuadra" disabled><option value="">Selecione a quadra</option></select>
        <label for="totemLote">LOTE</label>
        <select id="totemLote" disabled><option value="">Selecione o lote</option></select>
        <label for="totemService">Tipo de serviço (opcional)</label>
        <select id="totemService">
          <option value="">Selecione o tipo</option>
          <option>Ifood</option>
          <option>99 Entregas</option>
          <option>Uber Entregas</option>
          <option>Zé Delivery</option>
          <option>Mercado Livre</option>
          <option>Shopee</option>
          <option>TikTok Shop</option>
          <option>Restaurante</option>
          <option>Marmitaria</option>
          <option>Serviços Gerais</option>
          <option>Eletrecista</option>
          <option>Ar-Condicionado</option>
        </select>
        <button class="bigbtn" id="totemShowBtn" disabled>ABRIR LOCALIZAÇÃO</button>
      </div>
      <div class="status" id="totemStatus" role="status"></div>
    </div>
    <div id="totemSpeedBadge" class="speed-badge" style="display:none;align-self:center">
      <span class="ico">🚦</span>
      <span>Velocidade permitida dentro do Condomínio Sujeito a Multa!</span>
      <span class="val" id="totemSpeedValue">30 KM/h</span>
    </div>
    <div class="footer-area">
      <button id="totemAdminLink" style="background:transparent;border:0;color:var(--muted);font-size:12px;cursor:pointer;text-decoration:underline;padding:8px">🔒 Sou administrador</button>
    </div>
  </div>

  <div class="totem-result" id="totemResult" style="display:none">
    <div class="result-card">
      <div class="result-header">
        <div class="tag">📍 LOCALIZAÇÃO ENCONTRADA</div>
        <h2 id="totemResultTitle">Quadra A, Lote 01</h2>
        <div class="addr" id="totemResultAddr">—</div>
        <div class="proprietario" id="totemResultProprietario"></div>
      </div>
      <div class="nav-buttons">
        <a class="nav-btn gmaps" id="totemBtnGmaps" href="#" target="_blank" rel="noopener">
          <span class="ico">🗺️</span><span class="txt">Google Maps<small>Navegação padrão</small></span>
        </a>
        <a class="nav-btn waze" id="totemBtnWaze" href="#" target="_blank" rel="noopener">
          <span class="ico">🚗</span><span class="txt">Waze<small>Trânsito em tempo real</small></span>
        </a>
        <a class="nav-btn apple" id="totemBtnApple" href="#" target="_blank" rel="noopener">
          <span class="ico">🍎</span><span class="txt">Apple Maps<small>iPhone / iPad</small></span>
        </a>
        <button class="nav-btn copy" id="totemBtnCopy" type="button">
          <span class="ico">📋</span><span class="txt">Copiar endereço<small id="totemCopyPreview">—</small></span>
        </button>
      </div>
      <div class="speed-warn" id="totemResultSpeed" style="display:none">
        <span class="ico">🚦</span>
        <span>Velocidade máxima no condomínio: <strong id="totemResultSpeedVal">30 km/h</strong></span>
      </div>
      <div class="feedback" id="totemFeedback"></div>
      <button class="backbtn" id="totemBackBtn">↩ Escolher outro imóvel</button>
    </div>
  </div>
</div>

<!-- Modal de login do admin (bloqueia acesso não autorizado) -->
<div class="modal-overlay" id="adminModal">
  <div class="modal-card">
    <h3>🔒 Acesso administrativo</h3>
    <div class="sub">Digite usuário e senha para acessar o painel.</div>
    <label for="modalUser">Usuário</label>
    <input id="modalUser" autocomplete="username" placeholder="Usuário">
    <label for="modalPass">Senha</label>
    <input id="modalPass" type="password" autocomplete="current-password" placeholder="Senha">
    <div class="error" id="modalError"></div>
    <div class="actions">
      <button class="primary" id="modalLoginBtn" style="flex:1">Entrar</button>
      <button class="secondary" id="modalCancelBtn" style="flex:1">Cancelar</button>
    </div>
  </div>
</div>

<div id="appRoot">
<header>
  <div><h1>Indique-nos 6699209-4946 <a href="https://maps.google.com/" target="_blank" rel="noopener noreferrer" title="Abrir Google Maps" aria-label="Abrir Google Maps" style="display:inline-flex;align-items:center;vertical-align:middle;margin-left:7px;text-decoration:none;font-size:22px">📍</a></h1><p>Localização rápida e inteligente Condominial</p></div>
  <div class="header-right">
    <span id="cloudBadge" class="cloud-pill load" title="Status da conexão com a nuvem">☁️ conectando...</span>
    <span id="liveClock">--:--:--</span>
  </div>
  <nav class="no-print">
    <button class="active" data-view="portariaView">Portaria</button>
    <button data-view="displayView">Localização</button>
    <button data-view="portaoView">QR do Portão</button>
    <button data-view="cadastroView">Administradores</button>
    <button class="secondary" id="openDisplayBtn">Abrir segunda tela</button>
  </nav>
</header>
<main>
<section id="portariaView" class="view active">
  <div class="panel portaria-box">
    <span class="pill">ACESSO RÁPIDO</span>
    <h2>Para qual imóvel é a entrega ou serviço?</h2>
    <p>Selecione a rua/avenida ou a quadra e o lote.</p>
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
    <p class="hint">O prestador pode escanear este QR Code para abrir a localização.</p>
  </div>
</section>

<section id="portaoView" class="view">
  <div class="panel">
    <h2>QR Code fixo do portão</h2>
    <p class="hint">Imprima este QR Code e cole no portão. O prestador escaneia, escolhe rua/quadra/lote, e toca em <b>ABRIR LOCALIZAÇÃO</b>. Os dados vêm da nuvem, sempre atualizados.</p>
    <div style="text-align:center">
      <div class="qr-portao-preview" id="qrPortaoPreview"><div class="empty">Gerando QR Code do portão...</div></div>
      <div style="font-size:13px;color:var(--muted);margin-bottom:12px">Escaneie para testar</div>
    </div>
    <div class="actions" style="justify-content:center">
      <button class="primary" id="printPortaoBtn">🖨️ Imprimir QR do portão</button>
      <button class="secondary" id="downloadPortaoBtn">⬇️ Baixar PNG</button>
      <button class="secondary" id="copyPortaoUrlBtn">🔗 Copiar URL do totem</button>
    </div>
    <div class="status" id="portaoStatus" role="status" style="text-align:center"></div>
    <div style="margin-top:22px;padding:16px;background:#f5f8fc;border-radius:14px;border:1px solid var(--line)">
      <h3 style="margin-top:0">☁️ Dados na nuvem</h3>
      <p class="hint" style="margin:0">Este QR aponta para <code id="portaoUrlDisplay">—</code>. Como os dados estão no Supabase, <b>qualquer celular no mundo</b> verá a lista atualizada de imóveis que você cadastrou no PC.</p>
    </div>
  </div>
</section>

<section id="cadastroView" class="view">
  <div class="panel" id="loginPanel">
    <h2 id="authHeading">Acesso administrativo</h2>
    <p class="hint" id="authHint">Entre com usuário e senha.</p>
    <div id="setupFields" hidden>
      <label for="setupUser">Criar usuário administrador</label><input id="setupUser" autocomplete="username" placeholder="Ex.: portaria.admin">
      <label for="setupPass">Criar senha</label><input id="setupPass" type="password" autocomplete="new-password" placeholder="Mínimo de 6 caracteres">
      <label for="setupRecovery">Código de recuperação</label><input id="setupRecovery" type="password" autocomplete="off" placeholder="Palavra ou código">
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
    <label for="condoLogoFile">Logo de fundo (opcional)</label>
    <input id="condoLogoFile" type="file" accept="image/*">
    <div class="actions"><button class="green" id="saveCondoLogoBtn">Salvar logo</button><button class="secondary" id="clearCondoLogoBtn">Remover</button></div>
    <label for="slideFiles">Imagens (até 3)</label>
    <input id="slideFiles" type="file" accept="image/*" multiple>
    <div class="actions"><button class="green" id="saveSlidesBtn">Salvar imagens</button><button class="secondary" id="clearSlidesBtn">Remover</button></div>
    <label for="videoFile">Vídeo</label>
    <input id="videoFile" type="file" accept="video/mp4,video/webm,video/ogg">
    <div class="actions"><button class="green" id="saveVideoBtn">Salvar vídeo</button><button class="secondary" id="clearVideoBtn">Remover</button></div>
    <div class="status" id="slideStatus" role="status"></div>
    <div id="slidePreviews" class="grid"></div>
  </div>
  <div class="panel">
    <h2>Importar links de uma vez</h2>
    <p class="hint">Formato: <b>Quadra;Lote;Rua;Proprietário;CEP;Link</b> ou <b>Quadra;Lote;Link</b></p>
    <label for="bulkInput">Lista</label>
    <textarea id="bulkInput" placeholder="Quadra;Lote;Rua/Avenida;Proprietário;CEP;Link&#10;A;01;Avenida A;João da Silva;01310-100;https://maps.google.com/..."></textarea>
    <div class="actions">
      <button class="primary" id="importBtn">Importar lista</button>
      <button class="secondary" id="fileBtn">Arquivo CSV</button>
      <input id="csvFile" type="file" accept=".csv,text/csv,text/plain" hidden>
      <button class="secondary" id="exportBtn">Exportar CSV</button>
      <button class="danger" id="clearBtn">Apagar todos</button>
    </div>
    <div class="status" id="adminStatus" role="status"></div>
  </div>
  <div class="panel">
    <h2>Adicionar ou corrigir um imóvel</h2>
    <div class="grid">
      <div><label for="editQuadra">Quadra</label><input id="editQuadra" placeholder="Ex.: A"></div>
      <div><label for="editLote">Lote</label><input id="editLote" placeholder="Ex.: 01"></div>
      <div><label for="editRua">Rua / Avenida</label><input id="editRua" placeholder="Ex.: Avenida A"></div>
      <div><label for="editProprietario">Proprietário</label><input id="editProprietario" placeholder="Nome completo"></div>
      <div><label for="editCep">CEP</label><input id="editCep" placeholder="Ex.: 01310-100"></div>
      <div><label for="editVelocidade">Velocidade do condomínio (km/h)</label><input id="editVelocidade" type="number" min="5" max="80" value="30" placeholder="30"></div>
    </div>
    <label for="editUrl">Link da localização</label><input id="editUrl" type="url" placeholder="https://maps.google.com/...">
    <div class="actions"><button class="green" id="saveOneBtn">Salvar imóvel</button></div>
  </div>
  <div class="panel">
    <h2>Imóveis cadastrados <span class="pill" id="count">0 imóveis</span></h2>
    <div class="table-wrap"><table><thead><tr><th>Quadra</th><th>Lote</th><th>Rua / Avenida</th><th>Proprietário</th><th>CEP</th><th>Velocidade</th><th>Link</th><th>Ação</th></tr></thead><tbody id="recordsBody"><tr><td colspan="8" class="empty">Nenhum imóvel cadastrado.</td></tr></tbody></table></div>
  </div>
    <div class="panel" id="changePassPanel" hidden>
      <h2>Alterar senha</h2>
      <label for="currentPass">Senha atual</label><input id="currentPass" type="password">
      <label for="changeNewPass">Nova senha</label><input id="changeNewPass" type="password">
      <label for="changeRecovery">Código de recuperação</label><input id="changeRecovery" type="password">
      <div class="actions"><button class="primary" id="saveNewPassBtn">Salvar</button><button class="secondary" id="cancelChangePassBtn">Cancelar</button></div>
      <div class="status" id="changePassStatus" role="status"></div>
    </div>
  </div>
</section>
<section id="logsView" class="view">
  <div class="panel">
    <h2>Logs de navegação</h2>
    <div class="actions"><button class="secondary" id="exportLogsBtn">Exportar CSV</button><button class="danger" id="clearLogsBtn">Limpar</button></div>
    <div class="table-wrap"><table><thead><tr><th>Data</th><th>Ação</th><th>Detalhes</th></tr></thead><tbody id="logsBody"><tr><td colspan="3" class="empty">Nenhum registro.</td></tr></tbody></table></div>
  </div>
</section>
</main>
<button id="floatingReportBtn" type="button" title="Baixar relatório" style="position:fixed;right:18px;bottom:18px;z-index:9999;width:58px;height:50px;border:1px solid #d6b64b;border-radius:14px;background:linear-gradient(135deg,#fff4bd,#ffe58f);color:#243247;box-shadow:0 6px 18px #0003;font-size:28px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .15s ease">📂</button>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
/* ============================================================
   ⚙️ CONFIGURAÇÃO DO SUPABASE
   Substitua pelos valores do seu projeto Supabase.
   ============================================================ */
const SUPABASE_URL = 'https://uyakrrwqzvwlqhqjnscc.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV5YWtycndxenZ3bHFocWpuc2NjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTIyMDQxNTYsImV4cCI6MjEwNzc4MDE1Nn0.sL_yIcxaiYYEHRdLcKpeIRpf8lbjYxMiL0g0xKrCajc';

let supabaseClient = null;
function getSupabase(){
  if(!supabaseClient){
    if(!window.supabase || !window.supabase.createClient){console.error('[Supabase] Biblioteca não carregada');return null}
    if(!SUPABASE_URL || SUPABASE_URL.includes('COLE_AQUI')){console.error('[Supabase] Configure SUPABASE_URL e SUPABASE_ANON_KEY');return null}
    try{supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY)}catch(e){console.error('[Supabase]', e);return null}
  }
  return supabaseClient;
}

async function sbLoad(){
  const sb = getSupabase();
  if(!sb) return {data:null, error:new Error('Supabase não configurado')};
  return await sb.from('imoveis').select('*').order('quadra',{ascending:true}).order('lote',{ascending:true});
}
async function sbUpsert(r){
  const sb = getSupabase();
  if(!sb) return {error:new Error('Supabase não configurado')};
  const { data: existing, error: errSel } = await sb.from('imoveis').select('id').eq('quadra',r.quadra).eq('lote',r.lote).maybeSingle();
  if(errSel) return {error:errSel};
  if(existing){
    return await sb.from('imoveis').update({rua:r.rua, proprietario:r.proprietario, cep:r.cep||null, velocidade:r.velocidade||30, url:r.url, updated_at:new Date().toISOString()}).eq('id', existing.id);
  }
  return await sb.from('imoveis').insert({quadra:r.quadra, lote:r.lote, rua:r.rua, proprietario:r.proprietario, cep:r.cep||null, velocidade:r.velocidade||30, url:r.url});
}
async function sbDelete(quadra, lote){
  const sb = getSupabase();
  if(!sb) return {error:new Error('Supabase não configurado')};
  return await sb.from('imoveis').delete().eq('quadra',quadra).eq('lote',lote);
}

function updateCloudBadge(state, msg){
  const b = document.getElementById('cloudBadge');
  if(!b) return;
  b.className = 'cloud-pill ' + (state==='ok'?'':state);
  b.textContent = msg || (state==='ok'?'☁️ Nuvem OK':state==='err'?'⚠️ Erro':'☁️ ...');
  b.title = msg || '';
}

function extractGeo(url){
  let lat=null,lng=null;
  try{
    const u=new URL(url);
    const mAt=u.pathname.match(/@(-?\d+\.\d+),(-?\d+\.\d+)/);
    if(mAt){lat=parseFloat(mAt[1]);lng=parseFloat(mAt[2])}
    if(lat===null){
      const q=u.searchParams.get('q')||u.searchParams.get('query')||u.searchParams.get('ll')||u.searchParams.get('daddr')||u.searchParams.get('destination');
      if(q){const mQ=q.match(/^(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)$/);if(mQ){lat=parseFloat(mQ[1]);lng=parseFloat(mQ[2])}}
    }
    if(lat===null){
      const mPlace=u.pathname.match(/\/place\/(-?\d+\.\d+),(-?\d+\.\d+)/);
      if(mPlace){lat=parseFloat(mPlace[1]);lng=parseFloat(mPlace[2])}
    }
  }catch(e){}
  return {lat,lng};
}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function key(q,l){return String(q).trim().toLocaleLowerCase()+'|'+String(l).trim().toLocaleLowerCase()}
function validUrl(s){try{let u=new URL(s);return u.protocol==='https:'||u.protocol==='http:'}catch(e){return false}}
function simpleHash(text){let h=2166136261;for(let i=0;i<text.length;i++){h^=text.charCodeAt(i);h=Math.imul(h,16777619)}return (h>>>0).toString(16)}

const AUTH_STORAGE='portaria_facil_admin_auth_v1';
function getAuthData(){try{return JSON.parse(localStorage.getItem(AUTH_STORAGE)||'null')}catch(e){return null}}

/* NAV PAGE */
(function(){
  const params=new URLSearchParams(location.search);
  const nav=params.get('nav');
  if(!nav)return;
  const app=document.getElementById('appRoot');
  if(app)app.style.display='none';
  const navEl=document.getElementById('navPage');
  if(navEl)navEl.style.display='block';
  const parts=nav.split('|');
  const rua=parts[1]||'',quadra=parts[2]||'',lote=parts[3]||'',morador=parts[4]||'',coords=parts[5]||'',servico=parts[6]||'',linkOrig=parts[7]||'';
  const setText=(id,v)=>{const el=document.getElementById(id);if(el)el.textContent=v||'—'};
  setText('navProprietario',morador||'Não cadastrado');
  setText('navRua',rua||'Não cadastrada');
  setText('navQuadra',quadra);setText('navLote',lote);setText('navService',servico||'Não informado');
  let lat=null,lng=null;
  if(coords){const m=coords.match(/^(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)$/);if(m){lat=parseFloat(m[1]);lng=parseFloat(m[2])}}
  const displayAddress=[rua,quadra?'Quadra '+quadra:'',lote?'Lote '+lote:''].filter(Boolean).join(' — ');
  const fullAddress=displayAddress+(morador?' ('+morador+')':'');
  const gmaps=(lat!==null)?'https://www.google.com/maps/dir/?api=1&destination='+lat+','+lng:(linkOrig||('https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(fullAddress)));
  const elG=document.getElementById('navGmaps');if(elG)elG.href=gmaps;
  const waze=(lat!==null)?'https://waze.com/ul?ll='+lat+','+lng+'&navigate=yes':'https://waze.com/ul?q='+encodeURIComponent(fullAddress)+'&navigate=yes';
  const elW=document.getElementById('navWaze');if(elW)elW.href=waze;
  const apple=(lat!==null)?'https://maps.apple.com/?daddr='+lat+','+lng:'https://maps.apple.com/?q='+encodeURIComponent(fullAddress);
  const elA=document.getElementById('navApple');if(elA)elA.href=apple;
  const elO=document.getElementById('navOriginal');
  if(elO){if(linkOrig){elO.href=linkOrig;elO.style.display='flex'}else elO.style.display='none'}
  const preview=document.getElementById('navCopyPreview');
  if(preview){const t=fullAddress||'Endereço';preview.textContent=t.length>48?t.slice(0,48)+'…':t}
  const copyBtn=document.getElementById('navCopyBtn');
  const copyFb=document.getElementById('navCopyFeedback');
  if(copyBtn)copyBtn.addEventListener('click',async()=>{
    const texto=fullAddress||(lat!==null?(lat+','+lng):'');
    if(!texto){if(copyFb)copyFb.textContent='Nada para copiar.';return}
    try{await navigator.clipboard.writeText(texto);if(copyFb)copyFb.textContent='✅ Endereço copiado!'}
    catch(e){const ta=document.createElement('textarea');ta.value=texto;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');if(copyFb)copyFb.textContent='✅ Copiado!'}catch(_){if(copyFb)copyFb.textContent='❌ Falha.'}ta.remove()}
    setTimeout(()=>{if(copyFb)copyFb.textContent=''},3000);
  });
})();

/* APP PRINCIPAL */
(function(){
  const params=new URLSearchParams(location.search);
  if(params.get('nav')||params.get('portao'))return;

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

function openMediaDb(){return new Promise((resolve,reject)=>{if(!('indexedDB' in window)){reject(new Error('Sem IndexedDB'));return}const req=indexedDB.open(VIDEO_DB_NAME,1);req.onupgradeneeded=()=>{if(!req.result.objectStoreNames.contains(VIDEO_STORE))req.result.createObjectStore(VIDEO_STORE)};req.onsuccess=()=>resolve(req.result);req.onerror=()=>reject(req.error)})}
async function saveVideoBlob(file){const db=await openMediaDb();return new Promise((resolve,reject)=>{const tx=db.transaction(VIDEO_STORE,'readwrite');tx.objectStore(VIDEO_STORE).put(file,'presentation-video');tx.oncomplete=()=>{db.close();resolve()};tx.onerror=()=>{db.close();reject(tx.error)};tx.onabort=()=>{db.close();reject(tx.error)}})}
async function getVideoBlob(){const db=await openMediaDb();return new Promise((resolve,reject)=>{const tx=db.transaction(VIDEO_STORE,'readonly');const req=tx.objectStore(VIDEO_STORE).get('presentation-video');req.onsuccess=()=>{const r=req.result||null;db.close();resolve(r)};req.onerror=()=>{db.close();reject(req.error)}})}
async function deleteVideoBlob(){try{const db=await openMediaDb();await new Promise((resolve,reject)=>{const tx=db.transaction(VIDEO_STORE,'readwrite');tx.objectStore(VIDEO_STORE).delete('presentation-video');tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error);tx.onabort=()=>reject(tx.error)});db.close()}catch(e){}}
function broadcastMedia(){try{if('BroadcastChannel'in window){const c=new BroadcastChannel(CHANNEL);c.postMessage({type:'slides',images:slideImages,hasVideo:hasSlideVideo,logo:condoLogo});c.close()}}catch(e){}}
const LOG_STORAGE='portaria_facil_navigation_logs_v1';
const DELIVERY_STORAGE='portaria_facil_delivery_report_v1';
let deliveryEntries=[];try{deliveryEntries=JSON.parse(localStorage.getItem(DELIVERY_STORAGE)||'[]')}catch(e){deliveryEntries=[]}
const $=id=>document.getElementById(id);

async function refreshRecords(){
  updateCloudBadge('load','☁️ carregando...');
  const { data, error } = await sbLoad();
  if(error){console.error('[Supabase]', error);updateCloudBadge('err','⚠️ '+error.message);return false}
  records = (data||[]).map(r=>({quadra:r.quadra, lote:r.lote, rua:r.rua||'', proprietario:r.proprietario||'', cep:r.cep||'', velocidade:r.velocidade||30, url:r.url, id:r.id}));
  updateCloudBadge('ok','☁️ Nuvem OK ('+records.length+')');
  sortRecords(); renderSelectors(); renderTable();
  return true;
}

function recordDelivery(r){
 const now=new Date();const entry={date:now.toLocaleDateString('pt-BR'),time:now.toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit',second:'2-digit'}),serviceType:($('serviceTypeSelect')?.value)||'Não informado',quadra:r.quadra||'',lote:r.lote||'',rua:r.rua||'',proprietario:r.proprietario||'Não cadastrado'};
 deliveryEntries.push(entry);try{localStorage.setItem(DELIVERY_STORAGE,JSON.stringify(deliveryEntries))}catch(e){}
 logAction('Entrega registrada',`${entry.serviceType} — Q ${entry.quadra}, L ${entry.lote}`);
}
function downloadDeliveryReport(){
 const headers=['Data','Hora','Tipo de serviço','Quadra','Lote','Rua/Avenida','Nome do proprietário/morador'];
 const rows=deliveryEntries.map(e=>[e.date,e.time,e.serviceType,e.quadra,e.lote,e.rua,e.proprietario]);
 const csv='\uFEFF'+[headers,...rows].map(row=>row.map(v=>'"'+String(v??'').replace(/"/g,'""')+'"').join(';')).join('\r\n');
 const blob=new Blob([csv],{type:'text/csv;charset=utf-8;'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download='relatorio_entregas_'+new Date().toISOString().slice(0,10)+'.csv';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
}

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
function setStatus(id,msg,error=false){const el=$(id);if(!el)return;el.textContent=msg;el.style.color=error?'#b42318':'#12804a'}

let authData=null,adminAuthenticated=false;
authData = getAuthData();
function isAdminAuthenticated(){return adminAuthenticated}
function showAuthPanel(){
 const firstSetup=!authData;
 $('loginPanel').hidden=false;$('adminContent').hidden=true;$('setupFields').hidden=!firstSetup;$('loginFields').hidden=firstSetup;$('recoverFields').hidden=true;
 $('authHeading').textContent=firstSetup?'Criar acesso administrativo':'Acesso administrativo';
 $('authHint').textContent=firstSetup?'No primeiro acesso, crie usuário, senha e código de recuperação.':'Entre com usuário e senha.';
}
function grantAdmin(){adminAuthenticated=true;$('loginPanel').hidden=true;$('adminContent').hidden=false;refreshRecords();}
$('createAuthBtn').addEventListener('click',()=>{
 const username=$('setupUser').value.trim(),password=$('setupPass').value,recovery=$('setupRecovery').value;
 if(!username||password.length<6||recovery.length<4){setStatus('authStatus','Usuário, senha ≥6 e código ≥4.',true);return}
 authData={username:username.toLowerCase(),passwordHash:simpleHash(password),recoveryHash:simpleHash(recovery)};
 try{localStorage.setItem(AUTH_STORAGE,JSON.stringify(authData))}catch(e){}
 $('loginUser').value=username;$('loginPass').value='';showAuthPanel();setStatus('authStatus','Acesso criado.',false);
});
$('loginBtn').addEventListener('click',()=>{
 const username=$('loginUser').value.trim().toLowerCase(),password=$('loginPass').value;
 if(authData&&username===authData.username&&simpleHash(password)===authData.passwordHash){grantAdmin();setStatus('adminStatus','Autorizado.');logAction('Login','OK')}
 else setStatus('authStatus','Usuário ou senha incorretos.',true);
});
$('forgotPassBtn').addEventListener('click',()=>{$('loginFields').hidden=true;$('recoverFields').hidden=false;$('authStatus').textContent='';});
$('cancelRecoverBtn').addEventListener('click',()=>showAuthPanel());
$('resetPassBtn').addEventListener('click',()=>{
 const username=$('recoverUser').value.trim().toLowerCase(),code=$('recoverCode').value,newPass=$('newPass').value;
 if(!authData||username!==authData.username||simpleHash(code)!==authData.recoveryHash||newPass.length<6){setStatus('authStatus','Dados inválidos ou senha <6.',true);return}
 authData.passwordHash=simpleHash(newPass);try{localStorage.setItem(AUTH_STORAGE,JSON.stringify(authData))}catch(e){};
 $('loginUser').value=username;$('loginPass').value='';showAuthPanel();setStatus('authStatus','Senha redefinida.',false);
});
$('logoutBtn').addEventListener('click',()=>{adminAuthenticated=false;$('changePassPanel').hidden=true;showAuthPanel();setStatus('authStatus','Saiu.');});
$('changePassBtn').addEventListener('click',()=>{$('changePassPanel').hidden=!$('changePassPanel').hidden});
$('cancelChangePassBtn').addEventListener('click',()=>{$('changePassPanel').hidden=true});
$('saveNewPassBtn').addEventListener('click',()=>{
 const currentPass=$('currentPass').value,newPass=$('changeNewPass').value,recovery=$('changeRecovery').value;
 if(!authData||simpleHash(currentPass)!==authData.passwordHash||simpleHash(recovery)!==authData.recoveryHash||newPass.length<6){setStatus('changePassStatus','Dados inválidos.',true);return}
 authData.passwordHash=simpleHash(newPass);try{localStorage.setItem(AUTH_STORAGE,JSON.stringify(authData))}catch(e){};
 $('currentPass').value='';$('changeNewPass').value='';$('changeRecovery').value='';$('changePassPanel').hidden=true;setStatus('changePassStatus','Senha alterada.');
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
 $('recordsBody').innerHTML=records.length?records.map(r=>`<tr><td>${escapeHtml(r.quadra)}</td><td>${escapeHtml(r.lote)}</td><td>${escapeHtml(r.rua||'')}</td><td>${escapeHtml(r.proprietario||'')}</td><td>${escapeHtml(r.cep||'')}</td><td>${escapeHtml(r.velocidade||30)} km/h</td><td><a href="${escapeHtml(r.url)}" target="_blank" rel="noopener" style="color:var(--blue);font-weight:700">Abrir</a></td><td><button class="secondary" data-edit="${escapeHtml(key(r.quadra,r.lote))}" style="padding:8px 12px;font-size:12px">Editar</button> <button class="danger" data-remove="${escapeHtml(key(r.quadra,r.lote))}" style="padding:8px 12px;font-size:12px">Excluir</button></td></tr>`).join(''):'<tr><td colspan="8" class="empty">Nenhum imóvel cadastrado.</td></tr>';
}
function switchView(id){if(id==='cadastroView'&&!isAdminAuthenticated()){showAuthPanel()}document.querySelectorAll('.view').forEach(v=>v.classList.toggle('active',v.id===id));document.querySelectorAll('nav button').forEach(b=>b.classList.toggle('active',b.dataset.view===id));if(id==='displayView')renderCurrent();if(id==='logsView')renderLogs();if(id==='portaoView')renderPortaoQr();logAction('Navegação',id)}
function findRecord(q,l){return records.find(r=>key(r.quadra,r.lote)===key(q,l))}
function scheduleExpiry(){
 if(expiryTimer)clearTimeout(expiryTimer);
 expiryTimer=null;
 if(!current)return;
 const expiresAt=Number(current._expiresAt)||Date.now()+120000;
 const delay=expiresAt-Date.now();
 if(delay<=0){showRecord(null);return;}
 expiryTimer=setTimeout(()=>{if(current&&Number(current._expiresAt)===expiresAt){showRecord(null);logAction('Expirou','2 min')}},delay);
}
function showRecord(r){
 current=r?{...r,_expiresAt:Date.now()+120000}:null;
 try{if('BroadcastChannel'in window){let c=new BroadcastChannel(CHANNEL);c.postMessage({type:'current',record:current});c.close()}}catch(e){}
 renderCurrent();scheduleExpiry();
}
function updateClock(){try{const el=$('liveClock');if(el)el.textContent=new Date().toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit',second:'2-digit'})}catch(e){}}

function buildNavUrl(record){
  const geo=extractGeo(String(record.url||''));
  const coords=(geo.lat!==null&&geo.lng!==null)?(geo.lat+','+geo.lng):'';
  const svc=($('serviceTypeSelect')?.value)||'';
  const payload=['NAV',record.rua||'',record.quadra||'',record.lote||'',record.proprietario||'',coords,svc,record.url||''].join('|');
  const base=location.href.split('?')[0].split('#')[0];
  return base+'?nav='+encodeURIComponent(payload);
}

function startCountdown(){
 if(countdownInterval)clearInterval(countdownInterval);
 const el=$('countdown');if(!el)return;
 if(!current){el.hidden=true;return}
 el.hidden=false;
 const tick=()=>{const ms=Math.max(0,(Number(current?._expiresAt)||Date.now())-Date.now());const sec=Math.ceil(ms/1000);el.textContent=String(Math.floor(sec/60)).padStart(2,'0')+':'+String(sec%60).padStart(2,'0');if(sec<=0&&countdownInterval){clearInterval(countdownInterval);countdownInterval=null}};
 tick();countdownInterval=setInterval(tick,250);
}
async function imageToDataUrl(file){
 if(!file.type.startsWith('image/'))throw new Error('Imagens apenas.');
 const data=await new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result);reader.onerror=reject;reader.readAsDataURL(file)});
 const img=await new Promise((resolve,reject)=>{const im=new Image();im.onload=()=>resolve(im);im.onerror=reject;im.src=data});
 const scale=Math.min(1,1400/img.width,1000/img.height);const canvas=document.createElement('canvas');canvas.width=Math.max(1,Math.round(img.width*scale));canvas.height=Math.max(1,Math.round(img.height*scale));canvas.getContext('2d').drawImage(img,0,0,canvas.width,canvas.height);
 return canvas.toDataURL('image/jpeg',0.82);
}
$('saveCondoLogoBtn').addEventListener('click',async()=>{
 const file=$('condoLogoFile').files[0];if(!file){setStatus('slideStatus','Selecione uma imagem.',true);return}
 try{condoLogo=await imageToDataUrl(file);localStorage.setItem(CONDO_LOGO_STORAGE,condoLogo);const bg=$('displayBgLogo');if(bg)bg.style.backgroundImage=`url("${condoLogo}")`;broadcastMedia();setStatus('slideStatus','Logo salva.');$('condoLogoFile').value=''}catch(e){setStatus('slideStatus','Erro.',true)}
});
$('clearCondoLogoBtn').addEventListener('click',()=>{condoLogo='';try{localStorage.removeItem(CONDO_LOGO_STORAGE)}catch(e){}const bg=$('displayBgLogo');if(bg)bg.style.backgroundImage='none';broadcastMedia();setStatus('slideStatus','Logo removida.')});
$('saveSlidesBtn').addEventListener('click',async()=>{
 const files=[...$('slideFiles').files];if(!files.length){setStatus('slideStatus','Selecione até 3 imagens.',true);return}
 if(files.length>3){setStatus('slideStatus','Máx 3.',true);return}
 try{const converted=[];for(const f of files)converted.push(await imageToDataUrl(f));slideImages=converted;localStorage.setItem(SLIDES_STORAGE,JSON.stringify(slideImages));broadcastMedia();renderSlidePreviews();renderSlideshow();setStatus('slideStatus',`${slideImages.length} salva(s).`);$('slideFiles').value=''}catch(e){setStatus('slideStatus','Erro.',true)}
});
$('clearSlidesBtn').addEventListener('click',()=>{slideImages=[];try{localStorage.removeItem(SLIDES_STORAGE)}catch(e){}broadcastMedia();renderSlidePreviews();renderSlideshow();setStatus('slideStatus','Removidas.')});
$('saveVideoBtn').addEventListener('click',async()=>{
 const file=$('videoFile').files[0];if(!file){setStatus('slideStatus','Selecione vídeo.',true);return}
 if(!file.type.startsWith('video/')){setStatus('slideStatus','Inválido.',true);return}
 try{await saveVideoBlob(file);hasSlideVideo=true;localStorage.setItem(VIDEO_META_STORAGE,'1');broadcastMedia();renderSlidePreviews();await renderSlideshow();setStatus('slideStatus','Vídeo salvo.');$('videoFile').value=''}catch(e){setStatus('slideStatus','Erro.',true)}
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
 if(!current){$('qrOutput').innerHTML='<div class="empty">Aguardando.</div>';return}
 const qrUrl=buildNavUrl(current);
 if(!qrUrl){$('qrOutput').innerHTML='<div class="empty">Sem link.</div>';return}
 let generated=false;
 if(window.QRCode){
  try{new QRCode($('qrOutput'),{text:qrUrl,width:300,height:300,colorDark:'#000000',colorLight:'#ffffff',correctLevel:QRCode.CorrectLevel?QRCode.CorrectLevel.M:2});generated=!!$('qrOutput').querySelector('canvas, img')}catch(err){generated=false;$('qrOutput').innerHTML=''}
 }
 if(!generated){
  const img=document.createElement('img');img.alt='QR';img.width=300;img.height=300;
  img.style.width='300px';img.style.height='300px';img.style.maxWidth='min(65vw, 360px)';
  img.src='https://api.qrserver.com/v1/create-qr-code/?size=300x300&margin=10&data='+encodeURIComponent(qrUrl);
  img.onerror=()=>{$('qrOutput').innerHTML='<div class="empty">Sem conexão.</div>'};
  $('qrOutput').appendChild(img);
 }
}
$('ruaSelect').addEventListener('change',()=>{const street=$('ruaSelect').value;if($('quadraSelect').value&&!records.some(r=>r.quadra===$('quadraSelect').value&&(r.rua||'').trim()===street)&&street)$('quadraSelect').value='';$('loteSelect').value='';renderSelectors()});
$('quadraSelect').addEventListener('change',()=>{const q=$('quadraSelect').value,street=$('ruaSelect').value;if(street&&!records.some(r=>r.quadra===q&&(r.rua||'').trim()===street))$('ruaSelect').value='';$('loteSelect').value='';renderSelectors()});
$('loteSelect').addEventListener('change',()=>{const r=findRecord($('quadraSelect').value,$('loteSelect').value);if(r&&r.rua)$('ruaSelect').value=r.rua;renderSelectors();if(r)$('loteSelect').value=r.lote;});
$('showBtn').addEventListener('click',()=>{
 const q=$('quadraSelect').value,l=$('loteSelect').value;
 if(!q||!l){setStatus('portariaStatus','Selecione quadra e lote.',true);return}
 const r=findRecord(q,l);if(!r||($('ruaSelect').value&&(r.rua||'').trim()!==$('ruaSelect').value)){setStatus('portariaStatus','Não encontrado.',true);return}
 showRecord(r);recordDelivery(r);logAction('QR exibido',`Q ${r.quadra} L ${r.lote}`);setStatus('portariaStatus',`Exibindo Q ${r.quadra}, L ${r.lote}.`);
});
$('openDisplayBtn').addEventListener('click',()=>{
 const w=window.open(location.href.split('#')[0]+'#tela-prestador','_blank');
 if(!w){setStatus('portariaStatus','Pop-up bloqueado.',true);return}
 try{const req=w.document.documentElement.requestFullscreen;if(req){const result=req.call(w.document.documentElement);if(result&&result.catch)result.catch(()=>{});}}catch(_){}
 setStatus('portariaStatus','Segunda tela aberta.');
});
$('openMapBtn').addEventListener('click',()=>{if(current)window.open(current.url,'_blank','noopener')});
$('printQrBtn').addEventListener('click',()=>window.print());
document.querySelectorAll('nav button[data-view]').forEach(b=>b.addEventListener('click',()=>switchView(b.dataset.view)));

function parseLine(line){
  let parts=line.split(';');
  if(parts.length<3)parts=line.split(',');
  if(parts.length<3)return null;
  const q=parts.shift().trim(),l=parts.shift().trim();
  let rua='',proprietario='',cep='',url='';
  if(parts.length===1){url=parts[0].trim().replace(/^["']|["']$/g,'')}
  else if(parts.length>=4){rua=parts.shift().trim().replace(/^["']|["']$/g,'');proprietario=parts.shift().trim().replace(/^["']|["']$/g,'');cep=parts.shift().trim().replace(/^["']|["']$/g,'');url=parts.join(line.includes(';')?';':',').trim().replace(/^["']|["']$/g,'')}
  else if(parts.length>=3){rua=parts.shift().trim().replace(/^["']|["']$/g,'');proprietario=parts.shift().trim().replace(/^["']|["']$/g,'');url=parts.join(line.includes(';')?';':',').trim().replace(/^["']|["']$/g,'')}
  else{url=parts.join(line.includes(';')?';':',').trim().replace(/^["']|["']$/g,'')}
  if(!q||!l||!validUrl(url))return null;
  return {quadra:q,lote:l,rua,proprietario,cep,velocidade:30,url};
}
async function importText(text){
 const lines=text.replace(/^\uFEFF/,'').split(/\r?\n/).map(x=>x.trim()).filter(Boolean);
 let added=0,updated=0,skipped=0;
 for(const [i,line] of lines.entries()){
  if(i===0&&/quadra/i.test(line)&&/lote/i.test(line))continue;
  const r=parseLine(line);if(!r){skipped++;continue}
  const existing=findRecord(r.quadra,r.lote);
  const res = await sbUpsert(r);
  if(res.error){skipped++;continue}
  if(existing)updated++;else added++;
 }
 await refreshRecords();
 logAction('Import',`${added} novos, ${updated} atualizados, ${skipped} ignorados`);
 setStatus('adminStatus',`Import: ${added} novos, ${updated} atualizados, ${skipped} ignorados.`,false);
}
$('importBtn').addEventListener('click',async()=>{if(!$('bulkInput').value.trim()){setStatus('adminStatus','Cole lista.',true);return}await importText($('bulkInput').value)});
$('fileBtn').addEventListener('click',()=>$('csvFile').click());
$('csvFile').addEventListener('change',async e=>{const f=e.target.files[0];if(f){await importText(await f.text());e.target.value=''}});
$('saveOneBtn').addEventListener('click',async()=>{
 const q=$('editQuadra').value.trim(),l=$('editLote').value.trim(),rua=$('editRua').value.trim(),proprietario=$('editProprietario').value.trim(),cep=$('editCep').value.trim(),velocidade=parseInt($('editVelocidade').value)||30,url=$('editUrl').value.trim();
 if(!q||!l||!validUrl(url)){setStatus('adminStatus','Preencha quadra, lote e link.',true);return}
 const { error } = await sbUpsert({quadra:q,lote:l,rua,proprietario,cep,velocidade,url});
 if(error){setStatus('adminStatus','Erro: '+error.message,true);return}
 await refreshRecords();
 logAction('Imóvel salvo',`Q ${q} L ${l}`);setStatus('adminStatus',`Q ${q}, L ${l} salvo na nuvem.`);
 $('editQuadra').value='';$('editLote').value='';$('editRua').value='';$('editProprietario').value='';$('editCep').value='';$('editVelocidade').value='30';$('editUrl').value='';
});
$('recordsBody').addEventListener('click',async e=>{
 const ed=e.target.closest('[data-edit]'),rm=e.target.closest('[data-remove]');
 if(ed){const r=records.find(x=>key(x.quadra,x.lote)===ed.dataset.edit);if(r){$('editQuadra').value=r.quadra;$('editLote').value=r.lote;$('editRua').value=r.rua||'';$('editProprietario').value=r.proprietario||'';$('editCep').value=r.cep||'';$('editVelocidade').value=r.velocidade||30;$('editUrl').value=r.url;window.scrollTo({top:0,behavior:'smooth'})}}
 if(rm){const r=records.find(x=>key(x.quadra,x.lote)===rm.dataset.remove);if(r&&confirm(`Excluir Q ${r.quadra}, L ${r.lote}?`)){const { error } = await sbDelete(r.quadra, r.lote);if(error){setStatus('adminStatus','Erro: '+error.message,true);return}if(current&&key(current.quadra,current.lote)===key(r.quadra,r.lote))showRecord(null);await refreshRecords();logAction('Excluído',`Q ${r.quadra} L ${r.lote}`);setStatus('adminStatus','Excluído.')}}
});
$('clearBtn').addEventListener('click',async()=>{if(records.length&&confirm('Apagar TODOS os imóveis da nuvem?')){const sb=getSupabase();if(!sb)return;for(const r of records){await sb.from('imoveis').delete().eq('quadra',r.quadra).eq('lote',r.lote)}showRecord(null);await refreshRecords();setStatus('adminStatus','Todos apagados.')}});
$('exportBtn').addEventListener('click',()=>{
 const csv='\uFEFF'+[['Quadra','Lote','Rua/Avenida','Proprietário','CEP','Velocidade','Link'],...records.map(r=>[r.quadra,r.lote,r.rua||'',r.proprietario||'',r.cep||'',r.velocidade||30,r.url])].map(row=>row.map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(';')).join('\r\n');
 const blob=new Blob([csv],{type:'text/csv;charset=utf-8'}),a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='imoveis_condominio.csv';a.click();URL.revokeObjectURL(a.href);
});

function buildPortaoUrl(){const base=location.href.split('?')[0].split('#')[0];return base+'?portao=1'}
function renderPortaoQr(){
  const box=$('qrPortaoPreview');if(!box)return;
  const url=buildPortaoUrl();
  const el=$('portaoUrlDisplay');if(el)el.textContent=url;
  box.innerHTML='';
  let ok=false;
  if(window.QRCode){try{new QRCode(box,{text:url,width:280,height:280,colorDark:'#102b4e',colorLight:'#ffffff',correctLevel:QRCode.CorrectLevel.M});ok=!!box.querySelector('canvas, img')}catch(e){ok=false}}
  if(!ok){const img=document.createElement('img');img.width=280;img.height=280;img.src='https://api.qrserver.com/v1/create-qr-code/?size=280x280&margin=10&color=102b4e&data='+encodeURIComponent(url);box.appendChild(img)}
  setStatus('portaoStatus','QR pronto. Escaneie para testar.',false);
}
$('printPortaoBtn').addEventListener('click',()=>{
  const url=buildPortaoUrl();
  const win=window.open('','_blank');
  if(!win){setStatus('portaoStatus','Permita pop-ups.',true);return}
  win.document.write(`<!DOCTYPE html><html><head><meta charset="utf-8"><title>QR Portão</title><style>body{font-family:Arial;text-align:center;padding:40px;margin:0}h1{color:#102b4e;font-size:32px;margin:0 0 10px}h2{color:#1768c4;font-size:20px;margin:0 0 30px}p{color:#66758b;font-size:16px;max-width:500px;margin:20px auto;line-height:1.5}#qr{background:#fff;padding:24px;border:3px solid #102b4e;border-radius:20px;display:inline-block;margin:20px auto}img{display:block}.speed{margin-top:30px;padding:14px;background:#fff3c4;color:#6a4c00;border-radius:12px;font-weight:700;font-size:18px;display:inline-block}</style></head><body><h1>Residencial Reserva Celeste 3</h1><h2>📱 Escaneie para localizar o imóvel</h2><div id="qr"></div><p><b>Entregador:</b> escaneie o QR, escolha a quadra e o lote, e toque em <b>ABRIR LOCALIZAÇÃO</b>.</p><p class="speed">🚦 Velocidade máxima no condomínio: 30 KM/h</p><p style="font-size:13px;color:#999">${url}</p><script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"><\/script><script>new QRCode(document.getElementById('qr'),{text:${JSON.stringify(url)},width:320,height:320,colorDark:'#102b4e',colorLight:'#ffffff',correctLevel:QRCode.CorrectLevel.M});setTimeout(()=>window.print(),500);<\/script></body></html>`);
  win.document.close();
});
$('downloadPortaoBtn').addEventListener('click',()=>{
  const canvas=$('qrPortaoPreview').querySelector('canvas');
  const img=$('qrPortaoPreview').querySelector('img');
  if(canvas){const a=document.createElement('a');a.href=canvas.toDataURL('image/png');a.download='qr_portao.png';a.click();setStatus('portaoStatus','Baixado.',false)}
  else if(img){fetch(img.src).then(r=>r.blob()).then(b=>{const url=URL.createObjectURL(b);const a=document.createElement('a');a.href=url;a.download='qr_portao.png';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);setStatus('portaoStatus','Baixado.',false)}).catch(()=>setStatus('portaoStatus','Clique com botão direito → Salvar.',true))}
});
$('copyPortaoUrlBtn').addEventListener('click',async()=>{
  const url=buildPortaoUrl();
  try{await navigator.clipboard.writeText(url);setStatus('portaoStatus','URL copiada!',false)}
  catch(e){setStatus('portaoStatus','URL: '+url,false)}
});

if('BroadcastChannel'in window){const channel=new BroadcastChannel(CHANNEL);channel.onmessage=e=>{if(e.data?.type==='current'){current=e.data.record||null;renderCurrent();scheduleExpiry()}}}
if(location.hash==='#tela-prestador'){document.body.classList.add('display-mode');switchView('displayView');}

function renderSlidePreviews(){
 const box=$('slidePreviews');if(!box)return;
 const imageCards=slideImages.map((src,i)=>`<div style="border:1px solid var(--line);border-radius:10px;padding:8px;text-align:center"><img src="${src}" alt="Imagem ${i+1}" style="max-width:100%;height:110px;object-fit:contain"><div class="hint">Imagem ${i+1}</div></div>`);
 if(hasSlideVideo)imageCards.push('<div style="border:1px solid var(--line);border-radius:10px;padding:18px;text-align:center"><strong>Vídeo salvo</strong></div>');
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
     const img=document.createElement('img');img.alt='Imagem';img.src=item.src;img.onerror=()=>{if(token===slideRenderToken){index=(index+1)%items.length;showItem()}};box.appendChild(img);
     if(items.length>1)imageTimer=setTimeout(()=>{if(current||token!==slideRenderToken)return;index=(index+1)%items.length;showItem()},10000);
   }else{
     const video=document.createElement('video');video.src=item.src;video.autoplay=true;video.muted=true;video.defaultMuted=true;video.loop=items.length===1;video.playsInline=true;video.preload='auto';
     video.setAttribute('playsinline','');video.setAttribute('muted','');video.setAttribute('autoplay','');if(items.length===1)video.setAttribute('loop','');
     video.style.width='100%';video.style.height='100%';video.style.objectFit='contain';
     video.addEventListener('ended',()=>{if(items.length>1&&token===slideRenderToken&&!current){index=(index+1)%items.length;showItem()}});
     video.addEventListener('error',()=>{if(token===slideRenderToken){box.innerHTML='<div class="empty">Vídeo não suportado.</div>';if(items.length>1){imageTimer=setTimeout(()=>{index=(index+1)%items.length;showItem()},3000)}}});
     box.appendChild(video);
     const tryPlay=()=>{video.muted=true;video.defaultMuted=true;video.setAttribute('muted','');const p=video.play();if(p&&p.catch)p.catch(()=>{video.controls=true;video.setAttribute('controls','');});};
     video.addEventListener('loadedmetadata',tryPlay,{once:true});
     video.addEventListener('canplay',tryPlay,{once:true});
     tryPlay();
   }
 };
 showItem();
}

(async function init(){
  try{
    renderSlidePreviews();
    renderSlideshow();
    renderCurrent();
    updateClock();
    setInterval(updateClock,1000);
    showAuthPanel();
    await refreshRecords();

    const frBtn=document.getElementById('floatingReportBtn');
    if(frBtn)frBtn.addEventListener('click',()=>downloadDeliveryReport());

    const exLogs=$('exportLogsBtn');
    if(exLogs)exLogs.addEventListener('click',()=>{
      const csv='\uFEFF'+['Data','Ação','Detalhes'].join(';')+'\r\n'+logs.map(x=>[x.date,x.action,x.details||''].map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(';')).join('\r\n');
      const blob=new Blob([csv],{type:'text/csv;charset=utf-8'}),a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='logs_'+new Date().toISOString().slice(0,10)+'.csv';a.click();URL.revokeObjectURL(a.href);
    });
    const clLogs=$('clearLogsBtn');
    if(clLogs)clLogs.addEventListener('click',()=>{if(confirm('Apagar logs?')){logs=[];try{localStorage.removeItem(LOG_STORAGE)}catch(e){};renderLogs();}});
  }catch(err){console.error('[init]',err)}
})();

})();

/* TOTEM DO PORTÃO com login obrigatório */
(function(){
  const params=new URLSearchParams(location.search);
  if(!params.get('portao'))return;

  const app=document.getElementById('appRoot');
  if(app)app.style.display='none';
  const totem=document.getElementById('totemPage');
  if(totem)totem.style.display='block';

  const $=id=>document.getElementById(id);
  let records=[];
  let velocidadeGlobal = 30;

  async function loadFromCloud(){
    const { data, error } = await sbLoad();
    if(error){$('totemLoading').innerHTML='⚠️ Erro ao carregar: '+escapeHtml(error.message);return}
    records = (data||[]).map(r=>({quadra:r.quadra, lote:r.lote, rua:r.rua||'', proprietario:r.proprietario||'', cep:r.cep||'', velocidade:r.velocidade||30, url:r.url}));
    if(records.length===0){$('totemLoading').innerHTML='⚠️ Nenhum imóvel cadastrado ainda.';return}
    // Pega a velocidade mais comum (ou a primeira)
    velocidadeGlobal = records[0].velocidade || 30;
    $('totemLoading').style.display='none';
    $('totemFormFields').style.display='block';
    $('totemSpeedBadge').style.display='flex';
    $('totemSpeedValue').textContent = velocidadeGlobal + ' km/h';
    renderAllTotem();
  }

  function renderAllTotem(){
    const street=$('totemRua'),oldStreet=street.value;
    const streets=[...new Set(records.map(r=>(r.rua||'').trim()).filter(Boolean))].sort((a,b)=>a.localeCompare(b,'pt-BR',{numeric:true}));
    street.innerHTML='<option value="">Todas as ruas e avenidas</option>'+streets.map(v=>`<option value="${escapeHtml(v)}">${escapeHtml(v)}</option>`).join('');
    if(streets.includes(oldStreet))street.value=oldStreet;
    renderQuadrasTotem();
  }
  function renderQuadrasTotem(){
    const street=$('totemRua').value;
    const q=$('totemQuadra'),oldQ=q.value;
    const subset=records.filter(r=>!street||(r.rua||'').trim()===street);
    const qs=[...new Set(subset.map(r=>r.quadra))].sort((a,b)=>a.localeCompare(b,'pt-BR',{numeric:true}));
    q.innerHTML='<option value="">Selecione a quadra</option>'+qs.map(v=>`<option value="${escapeHtml(v)}">${escapeHtml(v)}</option>`).join('');
    q.disabled=!qs.length;if(qs.includes(oldQ))q.value=oldQ;
    renderLotesTotem();
  }
  function renderLotesTotem(){
    const street=$('totemRua').value,q=$('totemQuadra').value;
    const l=$('totemLote'),old=l.value;
    const ls=records.filter(r=>(!street||(r.rua||'').trim()===street)&&(!q||r.quadra===q)).sort((a,b)=>a.lote.localeCompare(b.lote,'pt-BR',{numeric:true}));
    l.innerHTML='<option value="">Selecione o lote</option>'+ls.map(r=>`<option value="${escapeHtml(r.lote)}">${escapeHtml(r.lote)}</option>`).join('');
    l.disabled=!q;if(ls.some(r=>r.lote===old))l.value=old;
    updateBtn();
  }
  function updateBtn(){
    const q=$('totemQuadra').value,l=$('totemLote').value;
    $('totemShowBtn').disabled=!(q&&l);
    const st=$('totemStatus');if(st)st.textContent='';
  }

  $('totemRua').addEventListener('change',()=>{renderQuadrasTotem();updateBtn()});
  $('totemQuadra').addEventListener('change',()=>{renderLotesTotem();updateBtn()});
  $('totemLote').addEventListener('change',updateBtn);

  $('totemShowBtn').addEventListener('click',()=>{
    const q=$('totemQuadra').value,l=$('totemLote').value,street=$('totemRua').value,service=$('totemService').value;
    if(!q||!l){$('totemStatus').textContent='Selecione quadra e lote.';return}
    const r=records.find(x=>key(x.quadra,x.lote)===key(q,l)&&(!street||(x.rua||'').trim()===street));
    if(!r){$('totemStatus').textContent='Imóvel não encontrado.';return}

    const geo=extractGeo(String(r.url||''));
    const hasCoords=(geo.lat!==null&&geo.lng!==null);
    const displayAddress=[r.rua, r.quadra?'Quadra '+r.quadra:'', r.lote?'Lote '+r.lote:''].filter(Boolean).join(' — ');
    const fullAddress=displayAddress+(r.proprietario?' — '+r.proprietario:'');

    const gmaps=hasCoords ? 'https://www.google.com/maps/dir/?api=1&destination='+geo.lat+','+geo.lng+'&travelmode=driving' : (r.url||('https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(fullAddress)));
    const waze=hasCoords ? 'https://waze.com/ul?ll='+geo.lat+','+geo.lng+'&navigate=yes' : 'https://waze.com/ul?q='+encodeURIComponent(fullAddress)+'&navigate=yes';
    const apple=hasCoords ? 'https://maps.apple.com/?daddr='+geo.lat+','+geo.lng+'&dirflg=d' : 'https://maps.apple.com/?q='+encodeURIComponent(fullAddress);

    const title=[r.quadra?'Quadra '+r.quadra:'', r.lote?'Lote '+r.lote:''].filter(Boolean).join(', ');
    $('totemResultTitle').textContent=title||'Imóvel';
    $('totemResultAddr').textContent=r.rua||'';
    $('totemResultProprietario').textContent=r.proprietario?('👤 '+r.proprietario):'';

    $('totemBtnGmaps').href=gmaps;
    $('totemBtnWaze').href=waze;
    $('totemBtnApple').href=apple;

    // Velocidade no resultado
    const speed = r.velocidade || velocidadeGlobal;
    $('totemResultSpeed').style.display='flex';
    $('totemResultSpeedVal').textContent = speed + ' km/h';

    const copyPreview=$('totemCopyPreview');
    if(copyPreview){const t=fullAddress;copyPreview.textContent=t.length>42?t.slice(0,42)+'…':t}

    const copyBtn=$('totemBtnCopy');
    const feedback=$('totemFeedback');
    copyBtn.onclick=async()=>{
      const texto=hasCoords?(geo.lat+','+geo.lng):fullAddress;
      try{await navigator.clipboard.writeText(texto);feedback.textContent='✅ Endereço copiado!'}
      catch(e){const ta=document.createElement('textarea');ta.value=texto;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');feedback.textContent='✅ Copiado!'}catch(_){feedback.textContent='❌ Falha.'}ta.remove()}
      setTimeout(()=>{feedback.textContent=''},4000);
    };

    try{
      const now=new Date();
      const entry={date:now.toLocaleDateString('pt-BR'),time:now.toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit',second:'2-digit'}),serviceType:service||'Não informado',quadra:r.quadra||'',lote:r.lote||'',rua:r.rua||'',proprietario:r.proprietario||'Não cadastrado'};
      const DELIVERY_STORAGE='portaria_facil_delivery_report_v1';
      let list=[];try{list=JSON.parse(localStorage.getItem(DELIVERY_STORAGE)||'[]')}catch(_){list=[]}
      list.push(entry);localStorage.setItem(DELIVERY_STORAGE,JSON.stringify(list));
    }catch(e){}

    $('totemForm').style.display='none';
    $('totemResult').style.display='block';
    window.scrollTo({top:0,behavior:'smooth'});
  });

  $('totemBackBtn').addEventListener('click',()=>{
    $('totemResult').style.display='none';
    $('totemForm').style.display='block';
    $('totemQuadra').value='';$('totemLote').value='';$('totemService').value='';
    renderLotesTotem();
  });

  // LOGIN OBRIGATÓRIO para "Sou administrador"
  $('totemAdminLink').addEventListener('click',e=>{
    e.preventDefault();
    const modal=document.getElementById('adminModal');
    modal.classList.add('active');
    $('modalUser').value='';
    $('modalPass').value='';
    $('modalError').textContent='';
    setTimeout(()=>$('modalUser').focus(),100);
  });

  $('modalCancelBtn').addEventListener('click',()=>{
    document.getElementById('adminModal').classList.remove('active');
  });

  $('modalLoginBtn').addEventListener('click',()=>{
    const authData = getAuthData();
    if(!authData){
      $('modalError').textContent='Nenhum administrador cadastrado ainda. Acesse o painel normalmente.';
      return;
    }
    const user=$('modalUser').value.trim().toLowerCase();
    const pass=$('modalPass').value;
    if(user===authData.username && simpleHash(pass)===authData.passwordHash){
      document.getElementById('adminModal').classList.remove('active');
      location.href=location.href.split('?')[0].split('#')[0];
    }else{
      $('modalError').textContent='Usuário ou senha incorretos.';
    }
  });

  // Enter no modal
  $('modalUser').addEventListener('keydown',e=>{if(e.key==='Enter')$('modalPass').focus()});
  $('modalPass').addEventListener('keydown',e=>{if(e.key==='Enter')$('modalLoginBtn').click()});

  loadFromCloud();
})();
</script>
</body>
</html>
