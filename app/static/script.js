  const API = 'http://localhost:8000';
  let isWaiting = false;
  let currentSessionId = generateSessionId();

  // ── Session ID generation ──
  function generateSessionId() {
    if (typeof crypto !== 'undefined' && crypto.randomUUID) return crypto.randomUUID();
    return Date.now().toString(36) + Math.random().toString(36).slice(2);
  }

  // ── Sidebar toggles ──
  function toggleSidebar() {
    document.getElementById('sidebar').classList.toggle('collapsed');
  }
  function toggleRightSidebar() {
    document.getElementById('right-sidebar').classList.toggle('collapsed');
  }

  // ── System info ──
  async function loadInfo() {
    const backendEl = document.getElementById('info-backend');
    const ollamaEl  = document.getElementById('info-ollama');

    // Run both requests in parallel; treat each failure independently
    const [infoResult, healthResult] = await Promise.allSettled([
      fetch(`${API}/info`,   { signal: AbortSignal.timeout(8000) }).then(r => r.json()),
      fetch(`${API}/health`, { signal: AbortSignal.timeout(6000) }).then(r => r.json()),
    ]);

    if (infoResult.status === 'fulfilled') {
      const data = infoResult.value;
      backendEl.className = 'info-badge online';
      backendEl.innerHTML = '<span class="dot"></span>Online';
      // model selector is populated by loadModels(); default is data.ollama_model
      document.getElementById('info-embed').textContent  = data.embedding_model;
      document.getElementById('info-chunks').textContent = data.total_chunks.toLocaleString();
      const uploadsEl = document.getElementById('info-uploads');
      if (data.uploaded_documents.length === 0) {
        uploadsEl.innerHTML = '<span class="info-empty">None yet</span>';
      } else {
        uploadsEl.innerHTML = data.uploaded_documents.map(d => `
          <div class="uploaded-file-item">
            <svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zm4 18H6V4h7v5h5v11z"/></svg>
            <div>
              <div>${escapeHtml(d.file_name)}</div>
              <div class="uploaded-file-chunks">${d.chunk_count} chunk${d.chunk_count !== 1 ? 's' : ''}</div>
            </div>
          </div>`).join('');
      }
    } else {
      backendEl.className = 'info-badge offline';
      backendEl.innerHTML = '<span class="dot"></span>Offline';
    }

    if (healthResult.status === 'fulfilled') {
      const online = healthResult.value.ollama;
      ollamaEl.className = online ? 'info-badge online' : 'info-badge offline';
      ollamaEl.innerHTML = `<span class="dot"></span>${online ? 'Online' : 'Offline'}`;
    } else {
      ollamaEl.className = 'info-badge offline';
      ollamaEl.innerHTML = '<span class="dot"></span>Offline';
    }
  }

  // ── Session list ──
  async function loadSessions() {
    try {
      const res = await fetch(`${API}/sessions`);
      if (!res.ok) return;
      const sessions = await res.json();
      renderSessionList(sessions);
    } catch { /* server not yet up */ }
  }

  function renderSessionList(sessions) {
    const list = document.getElementById('session-list');
    if (sessions.length === 0) {
      list.innerHTML = '<div class="session-empty">No previous chats</div>';
      return;
    }
    list.innerHTML = '';
    sessions.forEach(s => {
      const item = document.createElement('div');
      item.className = 'session-item' + (s.session_id === currentSessionId ? ' active' : '');
      item.dataset.sessionId = s.session_id;
      item.onclick = () => loadSession(s.session_id);
      item.innerHTML = `
        <div class="session-item-body">
          <div class="session-item-title">${escapeHtml(s.title)}</div>
          <div class="session-item-date">${formatDate(s.updated_at)}</div>
        </div>
        <button class="session-delete-btn" title="Delete chat" onclick="deleteSession(event, '${s.session_id}')">
          <svg viewBox="0 0 24 24"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/></svg>
        </button>`;
      list.appendChild(item);
    });
  }

  async function loadSession(sessionId) {
    if (sessionId === currentSessionId) return;
    currentSessionId = sessionId;

    const msgs = document.getElementById('messages');
    msgs.innerHTML = '';

    try {
      const res = await fetch(`${API}/sessions/${sessionId}/messages`);
      const messages = await res.json();
      messages.forEach(m => {
        addMessage('user', m.user_message);
        addMessage('bot', m.answer, m.sources);
      });
    } catch {
      addMessage('error', 'Could not load session messages.');
    }

    // Update active highlight
    document.querySelectorAll('.session-item').forEach(el => {
      el.classList.toggle('active', el.dataset.sessionId === sessionId);
    });
  }

  async function loadModels() {
    const sel = document.getElementById('model-select');
    try {
      const data = await fetch(`${API}/models`).then(r => r.json());
      sel.innerHTML = data.models.map(m =>
        `<option value="${m}"${m === data.default ? ' selected' : ''}>${m}</option>`
      ).join('');
    } catch {
      sel.innerHTML = `<option value="">Unavailable</option>`;
    }
  }

  loadSessions();
  loadInfo();
  loadModels();
  setInterval(loadInfo, 30000);

  // ── Auto-resize textarea ──
  const input = document.getElementById('user-input');
  input.addEventListener('input', () => {
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 120) + 'px';
  });
  input.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
  });

  // ── Send suggestion chip ──
  function sendSuggestion(btn) {
    input.value = btn.textContent;
    sendMessage();
  }

  // ── Delete session ──
  async function deleteSession(e, sessionId) {
    e.stopPropagation();
    if (!confirm('Delete this chat? This cannot be undone.')) return;
    await fetch(`${API}/sessions/${sessionId}`, { method: 'DELETE' });
    if (sessionId === currentSessionId) newChat();
    loadSessions();
  }

  // ── New chat ──
  function newChat() {
    currentSessionId = generateSessionId();
    const msgs = document.getElementById('messages');
    msgs.innerHTML = '';
    const w = document.createElement('div');
    w.id = 'welcome';
    w.className = 'welcome';
    w.innerHTML = `
      <div class="welcome-icon">
        <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/></svg>
      </div>
      <h2>How can I help you?</h2>
      <p>Ask me anything about the ELTE Faculty of Informatics — curriculum, prerequisites, exam rules, registration, or admissions.</p>
      <div class="suggestion-chips">
        <button class="chip" onclick="sendSuggestion(this)">What is a strong prerequisite?</button>
        <button class="chip" onclick="sendSuggestion(this)">How does Neptun handle registration?</button>
        <button class="chip" onclick="sendSuggestion(this)">What BSc programs are available?</button>
        <button class="chip" onclick="sendSuggestion(this)">What is a weak prerequisite?</button>
      </div>`;
    msgs.appendChild(w);
    // Clear active state in sidebar
    document.querySelectorAll('.session-item').forEach(el => el.classList.remove('active'));
  }

  // ── Send message ──
  async function sendMessage() {
    const text = input.value.trim();
    if (!text || isWaiting) return;

    const welcome = document.getElementById('welcome');
    if (welcome) welcome.remove();

    addMessage('user', text);
    input.value = '';
    input.style.height = 'auto';

    const typingEl = addTyping();
    setWaiting(true);

    try {
      const res = await fetch(`${API}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, session_id: currentSessionId, model: document.getElementById('model-select').value || undefined })
      });

      typingEl.remove();

      if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: 'Server error' }));
        addMessage('error', err.detail || `Error ${res.status}`);
        return;
      }

      const data = await res.json();
      addMessage('bot', data.answer, data.sources, data.response_ms);
      loadSessions(); // refresh sidebar

    } catch (err) {
      typingEl.remove();
      addMessage('error', 'Could not reach the server. Make sure the backend is running.');
    } finally {
      setWaiting(false);
    }
  }

  function setWaiting(val) {
    isWaiting = val;
    document.getElementById('send-btn').disabled = val;
    input.disabled = val;
  }

  // ── Helpers ──
  function escapeHtml(text) {
    const d = document.createElement('div');
    d.appendChild(document.createTextNode(text));
    return d.innerHTML;
  }

  function formatDate(iso) {
    const d = new Date(iso);
    const now = new Date();
    if (d.toDateString() === now.toDateString()) {
      return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
    return d.toLocaleDateString([], { month: 'short', day: 'numeric' });
  }

  // ── Append a message bubble ──
  function addMessage(role, text, sources = [], response_ms = 0) {
    const msgs = document.getElementById('messages');

    const wrap = document.createElement('div');
    wrap.className = `msg ${role === 'user' ? 'user' : role === 'error' ? 'bot error' : 'bot'}`;

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = role === 'user' ? 'You' : 'IK';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = text;

    // Response time
    if (role === 'bot' && response_ms > 0) {
      const t = document.createElement('div');
      t.className = 'response-time';
      const secs = (response_ms / 1000).toFixed(1);
      t.innerHTML = `<svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm.01 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67V7z"/></svg>${secs}s`;
      bubble.appendChild(t);
    }

    // Sources
    if (sources && sources.length > 0) {
      const srcWrap = document.createElement('div');
      srcWrap.className = 'sources';

      const toggle = document.createElement('button');
      toggle.className = 'sources-toggle';
      const uniqueFiles = new Set(sources.map(s => s.file)).size;
      toggle.innerHTML = `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M10 17l5-5-5-5v10z"/></svg>retrieved ${sources.length} chunk${sources.length > 1 ? 's' : ''} from ${uniqueFiles} file${uniqueFiles > 1 ? 's' : ''}`;

      const list = document.createElement('div');
      list.className = 'sources-list';

      // Deduplicate by file name
      const seen = new Set();
      sources.forEach(s => {
        if (!seen.has(s.file)) {
          seen.add(s.file);
          const tag = document.createElement('a');
          tag.className = 'source-tag';
          tag.textContent = s.file;
          tag.href = `${API}/source/${encodeURIComponent(s.file)}`;
          tag.target = '_blank';
          tag.rel = 'noopener';
          list.appendChild(tag);
        }
      });

      toggle.addEventListener('click', () => {
        list.classList.toggle('visible');
        toggle.classList.toggle('open');
      });

      srcWrap.appendChild(toggle);
      srcWrap.appendChild(list);
      bubble.appendChild(srcWrap);
    }

    wrap.appendChild(avatar);
    wrap.appendChild(bubble);
    msgs.appendChild(wrap);
    msgs.scrollTop = msgs.scrollHeight;
    return wrap;
  }

  // ── File upload ──
  const fileInput = document.getElementById('file-input');
  fileInput.addEventListener('change', async () => {
    const file = fileInput.files[0];
    if (!file) return;
    fileInput.value = '';

    const toast = document.getElementById('upload-toast');
    const uploadBtn = document.getElementById('upload-btn');
    uploadBtn.disabled = true;

    toast.className = 'indexing';
    toast.textContent = `Indexing "${file.name}"…`;

    const fd = new FormData();
    fd.append('file', file);

    try {
      const res = await fetch(`${API}/upload`, { method: 'POST', body: fd });
      const data = await res.json();

      if (!res.ok) {
        toast.className = 'error';
        toast.textContent = `Upload failed: ${data.detail || res.status}`;
      } else if (data.status === 'already_indexed') {
        toast.className = 'duplicate';
        toast.textContent = `"${data.file_name}" is already in the knowledge base.`;
      } else {
        toast.className = 'success';
        toast.textContent = `Added ${data.chunk_count} chunks from "${data.file_name}" — you can now ask questions about it.`;
        loadInfo();
      }
    } catch {
      toast.className = 'error';
      toast.textContent = 'Upload failed — could not reach the server.';
    } finally {
      uploadBtn.disabled = false;
      setTimeout(() => { toast.className = ''; toast.textContent = ''; }, 8000);
    }
  });

  // ── Typing indicator ──
  function addTyping() {
    const msgs = document.getElementById('messages');
    const wrap = document.createElement('div');
    wrap.className = 'msg bot typing';

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = 'IK';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';

    wrap.appendChild(avatar);
    wrap.appendChild(bubble);
    msgs.appendChild(wrap);
    msgs.scrollTop = msgs.scrollHeight;
    return wrap;
  }
