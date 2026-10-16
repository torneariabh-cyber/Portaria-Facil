<!DOCTYPE html>
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
