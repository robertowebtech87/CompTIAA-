/* ── Quiz Engine ────────────────────────────────────────────── */

let currentIndex = 0;
let answers = {};       // { questionId: choiceId }
let questionCache = {}; // { questionId: questionData }
let timerInterval = null;
let timeElapsed = 0;
let timeLimitSecs = 0;

// Per-question timer
let perQInterval = null;
let perQRemaining = 90;

/* ── Bootstrap ───────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  if (typeof QUESTION_IDS === 'undefined') return; // not on quiz page

  timeLimitSecs = TIME_LIMIT;
  buildDots();
  loadQuestion(0);
  startTimer();

  // Simulation mode — disable prev button and lock dot navigation
  if (typeof SIM_MODE !== 'undefined' && SIM_MODE) {
    const prevBtn = document.getElementById('btn-prev');
    if (prevBtn) prevBtn.style.display = 'none';
  }
});

/* ── Timer ───────────────────────────────────────────────────── */
function startTimer() {
  const el = document.getElementById('timer');
  const wrap = document.querySelector('.timer-wrap');
  timerInterval = setInterval(() => {
    timeElapsed++;
    const remaining = timeLimitSecs - timeElapsed;
    const m = Math.floor(Math.abs(remaining) / 60);
    const s = Math.abs(remaining) % 60;
    el.textContent = `${remaining < 0 ? '-' : ''}${m}:${String(s).padStart(2, '0')}`;
    if (remaining <= 120) wrap.classList.add('warning');
    if (remaining <= 0) autoSubmit();
  }, 1000);
}

function autoSubmit() {
  clearInterval(timerInterval);
  confirmSubmit();
}

/* ── Dots ────────────────────────────────────────────────────── */
function buildDots() {
  const container = document.getElementById('dots');
  QUESTION_IDS.forEach((_, i) => {
    const d = document.createElement('div');
    d.className = 'dot' + (i === 0 ? ' current' : '');
    // In simulation mode dots are display only — no clicking back
    if (typeof SIM_MODE === 'undefined' || !SIM_MODE) {
      d.onclick = () => goToQuestion(i);
    } else {
      d.style.cursor = 'default';
    }
    container.appendChild(d);
  });
}

function updateDots() {
  document.querySelectorAll('.dot').forEach((d, i) => {
    d.className = 'dot';
    if (answers[QUESTION_IDS[i]] !== undefined) d.classList.add('answered');
    if (i === currentIndex) d.classList.add('current');
  });
}

/* ── Load Question ───────────────────────────────────────────── */
async function loadQuestion(index) {
  currentIndex = index;
  const qid = QUESTION_IDS[index];
  const area = document.getElementById('question-area');
  area.innerHTML = '<div class="loading-pulse">Loading…</div>';

  if (!questionCache[qid]) {
    const res = await fetch(`/api/question/${qid}`);
    questionCache[qid] = await res.json();
  }

  const q = questionCache[qid];
  const letters = ['A', 'B', 'C', 'D'];
  const selectedId = answers[qid];

  const isMulti = q.multi_select;
  const correctCount = q.correct_count || 1;
  const selectedIds = answers[qid] || (isMulti ? [] : null);

  area.innerHTML = `
    <p class="question-text">${q.text}</p>
    ${isMulti ? `<div class="multi-select-hint">Select <strong>${correctCount}</strong> answers</div>` : ''}
    <div class="choices-list">
      ${q.choices.map((c, i) => {
        const isSelected = isMulti
          ? (Array.isArray(selectedIds) && selectedIds.includes(c.id))
          : selectedIds == c.id;
        return `
          <button class="choice-btn ${isSelected ? 'selected' : ''}"
                  onclick="${isMulti ? `selectMultiAnswer(${qid}, ${c.id}, ${correctCount}, this)` : `selectAnswer(${qid}, ${c.id}, this)`}">
            <span class="choice-letter ${isMulti ? 'multi' : ''}">${letters[i]}</span>
            ${c.text}
          </button>
        `;
      }).join('')}
    </div>
  `;

  // Update counter, domain, progress
  document.getElementById('q-counter').textContent = `${index + 1} / ${QUESTION_IDS.length}`;
  document.getElementById('domain-tag').textContent = q.domain || '';

  // Per-question timer
  if (typeof PER_Q_TIMER !== 'undefined' && PER_Q_TIMER) {
    startPerQTimer();
  }
  document.getElementById('progress-bar').style.width = `${((index + 1) / QUESTION_IDS.length) * 100}%`;

  // Nav buttons
  document.getElementById('btn-prev').disabled = index === 0;
  document.getElementById('btn-next').textContent = index === QUESTION_IDS.length - 1 ? 'Review →' : 'Next →';

  // Show submit on last
  const submitBtn = document.getElementById('btn-submit');
  submitBtn.style.display = index === QUESTION_IDS.length - 1 ? 'block' : 'none';

  updateDots();
}

/* ── Per-Question Timer ──────────────────────────────────────────── */
function startPerQTimer() {
  clearInterval(perQInterval);
  perQRemaining = PER_Q_SECONDS;

  // Create or reset the timer bar
  let bar = document.getElementById('per-q-bar');
  if (!bar) {
    const wrap = document.createElement('div');
    wrap.className = 'per-q-timer-wrap';
    wrap.innerHTML = `
      <div class="per-q-bar-track">
        <div class="per-q-bar-fill" id="per-q-bar"></div>
      </div>
      <span class="per-q-label" id="per-q-label">90s</span>
    `;
    const area = document.getElementById('question-area');
    area.parentNode.insertBefore(wrap, area);
    bar = document.getElementById('per-q-bar');
  }
  bar.style.width = '100%';
  bar.className = 'per-q-bar-fill';
  document.getElementById('per-q-label').textContent = `${PER_Q_SECONDS}s`;

  perQInterval = setInterval(() => {
    perQRemaining--;
    const pct = (perQRemaining / PER_Q_SECONDS) * 100;
    bar.style.width = pct + '%';
    document.getElementById('per-q-label').textContent = `${perQRemaining}s`;

    if (perQRemaining <= 10) bar.classList.add('per-q-warning');
    if (perQRemaining <= 0) {
      clearInterval(perQInterval);
      bar.style.width = '0%';
      document.getElementById('per-q-label').textContent = '⏰';
      // Auto advance to next question
      setTimeout(() => nextQuestion(), 500);
    }
  }, 1000);
}

function stopPerQTimer() {
  clearInterval(perQInterval);
}

function selectAnswer(qid, choiceId, btn) {
  answers[qid] = choiceId;
  document.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
  updateDots();
  if (typeof PER_Q_TIMER !== 'undefined' && PER_Q_TIMER) stopPerQTimer();
}

function selectMultiAnswer(qid, choiceId, correctCount, btn) {
  if (typeof PER_Q_TIMER !== 'undefined' && PER_Q_TIMER) stopPerQTimer();
  if (!Array.isArray(answers[qid])) answers[qid] = [];
  const idx = answers[qid].indexOf(choiceId);
  if (idx === -1) {
    // Add if not already at limit
    if (answers[qid].length < correctCount) {
      answers[qid].push(choiceId);
      btn.classList.add('selected');
    } else {
      // Flash the button to indicate limit reached
      btn.classList.add('limit-flash');
      setTimeout(() => btn.classList.remove('limit-flash'), 400);
    }
  } else {
    // Deselect
    answers[qid].splice(idx, 1);
    btn.classList.remove('selected');
  }
  updateDots();
}

function nextQuestion() {
  if (currentIndex < QUESTION_IDS.length - 1) loadQuestion(currentIndex + 1);
}

function prevQuestion() {
  if (currentIndex > 0) loadQuestion(currentIndex - 1);
}

function goToQuestion(i) {
  loadQuestion(i);
}

/* ── Submit ──────────────────────────────────────────────────── */
function submitQuiz() {
  const unanswered = QUESTION_IDS.filter(id => answers[id] === undefined).length;
  const msg = document.getElementById('unanswered-msg');
  msg.textContent = unanswered > 0
    ? `You have ${unanswered} unanswered question${unanswered > 1 ? 's' : ''}. You can go back or submit now.`
    : 'All questions answered. Ready to submit?';
  document.getElementById('confirm-overlay').style.display = 'flex';
}

function closeConfirm() {
  document.getElementById('confirm-overlay').style.display = 'none';
}

async function confirmSubmit() {
  clearInterval(timerInterval);
  closeConfirm();

  const btn = document.getElementById('btn-submit');
  if (btn) { btn.textContent = 'Submitting…'; btn.disabled = true; }

  const res = await fetch('/api/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      answers,
      question_ids: QUESTION_IDS,
      time_taken: timeElapsed,
      exam: typeof EXAM !== 'undefined' ? EXAM : 'core1'
    })
  });

  const data = await res.json();
  window.location.href = `/results/${data.attempt_id}`;
}

/* ── Results filter ──────────────────────────────────────────── */
function filterResults(type, btn) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('.qa-item').forEach(el => {
    if (type === 'all') el.style.display = '';
    else el.style.display = el.dataset.status === type ? '' : 'none';
  });
}

function toggleQA(header) {
  header.parentElement.classList.toggle('open');
}

/* ── Admin toggle ────────────────────────────────────────────── */
async function toggleQ(qid) {
  const res = await fetch(`/admin/question/${qid}/toggle`, { method: 'POST' });
  const data = await res.json();
  const row = document.getElementById(`qrow-${qid}`);
  const status = document.getElementById(`status-${qid}`);
  if (data.active) {
    row.classList.remove('inactive');
    status.textContent = 'Active';
    status.className = 'admin-status active';
  } else {
    row.classList.add('inactive');
    status.textContent = 'Inactive';
    status.className = 'admin-status off';
  }
}