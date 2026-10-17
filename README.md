const STORAGE = {
  properties: 'portariaFacil_properties',
  media: 'portariaFacil_media',
  reports: 'portariaFacil_reports',
  current: 'portariaFacil_current'
};

const $ = id => document.getElementById(id);

function readStorage(key, fallback) {
  try {
    const value = localStorage.getItem(key);
    return value === null ? fallback : JSON.parse(value);
  } catch (error) {
    return fallback;
  }
}

function writeStorage(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
    return true;
  } catch (error) {
    console.error('Não foi possível salvar:', error);
    return false;
  }
}

function escapeHtml(value) {
  return String(value ?? '').replace(/[&<>"']/g, char => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  })[char]);
}

function setStatus(id, message, isError = false) {
  const element = $(id);
  if (!element) return;
  element.textContent = message;
  element.style.color = isError ? '#b42318' : '#12804a';
}

function getProperties() {
  const data = readStorage(STORAGE.properties, []);
  return Array.isArray(data) ? data : [];
}

function saveProperties(properties) {
  return writeStorage(STORAGE.properties, properties);
}

function getMedia() {
  const data = readStorage(STORAGE.media, {
    links: [],
    interval: 10
  });

  return data && Array.isArray(data.links)
    ? data
    : { links: [], interval: 10 };
}

function getReports() {
  const data = readStorage(STORAGE.reports, []);
  return Array.isArray(data) ? data : [];
}

function logAction(property, action) {
  const reports = getReports();

  reports.unshift({
    date: new Date().toLocaleString('pt-BR'),
    rua: property?.rua || '',
    quadra: property?.quadra || '',
    lote: property?.lote || '',
    action
  });

  writeStorage(STORAGE.reports, reports.slice(0, 5000));
}

function parsePropertyLines(text) {
  return text.split(/\r?\n/)
    .map(line => line.trim())
    .filter(Boolean)
    .map(line => {
      const parts = line.split(';').map(item => item.trim());

      return {
        rua: parts[0] || '',
        quadra: parts[1] || '',
        lote: parts[2] || ''
      };
    })
    .filter(item => item.rua && item.quadra && item.lote);
}

function populatePropertySelectors() {
  const properties = getProperties();
  const ruaSelect = $('ruaSelect');
  const quadraSelect = $('quadraSelect');
  const loteSelect = $('loteSelect');

  if (!ruaSelect || !quadraSelect || !loteSelect) return;

  const selectedRua = ruaSelect.value;
  const selectedQuadra = quadraSelect.value;

  const ruas = [...new Set(properties.map(item => item.rua))]
    .sort((a, b) => a.localeCompare(b, 'pt-BR', { numeric: true }));

  ruaSelect.innerHTML =
    '<option value="">Todas as ruas e avenidas</option>' +
    ruas.map(rua =>
      `<option value="${escapeHtml(rua)}">${escapeHtml(rua)}</option>`
    ).join('');

  if (ruas.includes(selectedRua)) ruaSelect.value = selectedRua;

  const filtradas = properties.filter(item =>
    !ruaSelect.value || item.rua === ruaSelect.value
  );

  const quadras = [...new Set(filtradas.map(item => item.quadra))]
    .sort((a, b) => a.localeCompare(b, 'pt-BR', { numeric: true }));

  quadraSelect.innerHTML =
    '<option value="">Selecione a quadra</option>' +
    quadras.map(quadra =>
      `<option value="${escapeHtml(quadra)}">${escapeHtml(quadra)}</option>`
    ).join('');

  if (quadras.includes(selectedQuadra)) {
    quadraSelect.value = selectedQuadra;
  }

  populateLotSelector();
}

function populateLotSelector() {
  const rua = $('ruaSelect').value;
  const quadra = $('quadraSelect').value;
  const loteSelect = $('loteSelect');

  const properties = getProperties().filter(item =>
    (!rua || item.rua === rua) &&
    (!quadra || item.quadra === quadra)
  );

  const lotes = [...new Set(properties.map(item => item.lote))]
    .sort((a, b) => a.localeCompare(b, 'pt-BR', { numeric: true }));

  loteSelect.innerHTML =
    '<option value="">Selecione o lote</option>' +
    lotes.map(lote =>
      `<option value="${escapeHtml(lote)}">${escapeHtml(lote)}</option>`
    ).join('');

  loteSelect.disabled = !quadra || lotes.length === 0;
}

function showView(viewId) {
  document.querySelectorAll('.view').forEach(view => {
    view.classList.toggle('active', view.id === viewId);
  });

  document.querySelectorAll('nav button[data-view]').forEach(button => {
    button.classList.toggle('active', button.dataset.view === viewId);
  });

  if (viewId === 'displayView') {
    updateDisplay();
  }
}

function getSelectedProperty() {
  const rua = $('ruaSelect').value;
  const quadra = $('quadraSelect').value;
  const lote = $('loteSelect').value;

  if (!quadra || !lote) return null;

  return getProperties().find(item =>
    item.quadra === quadra &&
    item.lote === lote &&
    (!rua || item.rua === rua)
  ) || null;
}

function getLocationUrl(property) {
  const base = 'https://www.google.com/maps/search/?api=1&query=';
  const query = [
    property.rua,
    'Quadra ' + property.quadra,
    'Lote ' + property.lote,
    'Residencial Reserva Celeste 3, Sinop, MT'
  ].join(', ');

  return base + encodeURIComponent(query);
}

function updateDisplay() {
  const property = readStorage(STORAGE.current, null);
  const screen = $('displayScreen');

  if (!property) {
    $('displayTitle').textContent = 'Aguardando localização';
    $('displayRua').textContent = '—';
    $('displayQuadra').textContent = '—';
    $('displayLote').textContent = '—';
    $('qrOutput').innerHTML = '';
    screen.classList.remove('showing-qr');
    return;
  }

  $('displayTitle').textContent = 'Localização da entrega';
  $('displayRua').textContent = property.rua;
  $('displayQuadra').textContent = property.quadra;
  $('displayLote').textContent = property.lote;

  screen.classList.add('showing-qr');

  const url = getLocationUrl(property);
  $('displayUrl').textContent = url;

  const output = $('qrOutput');
  output.innerHTML = '';

  if (typeof QRCode !== 'undefined') {
    new QRCode(output, {
      text: url,
      width: 300,
      height: 300,
      colorDark: '#102b4e',
      colorLight: '#ffffff',
      correctLevel: QRCode.CorrectLevel.H
    });
  } else {
    output.textContent = 'Não foi possível carregar o gerador de QR Code.';
  }

  $('countdown').hidden = false;
  $('countdown').textContent = 'QR Code pronto';
}
