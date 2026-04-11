/* ── Quiz Engine ────────────────────────────────────────────── */

let currentIndex = 0;
let answers = {};       // { questionId: choiceId }
let questionCache = {}; // { questionId: questionData }
let timerInterval = null;
let timeElapsed = 0;
let timeLimitSecs = 0;

/* ── Bootstrap ───────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  if (typeof QUESTION_IDS === 'undefined') return; // not on quiz page

  timeLimitSecs = TIME_LIMIT;
  buildDots();
  loadQuestion(0);
  startTimer();
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
    d.onclick = () => goToQuestion(i);
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

  area.innerHTML = `
    <p class="question-text">${q.text}</p>
    <div class="choices-list">
      ${q.choices.map((c, i) => `
        <button class="choice-btn ${selectedId == c.id ? 'selected' : ''}"
                onclick="selectAnswer(${qid}, ${c.id}, this)">
          <span class="choice-letter">${letters[i]}</span>
          ${c.text}
        </button>
      `).join('')}
    </div>
  `;

  // Update counter, domain, progress
  document.getElementById('q-counter').textContent = `${index + 1} / ${QUESTION_IDS.length}`;
  document.getElementById('domain-tag').textContent = q.domain || '';
  document.getElementById('progress-bar').style.width = `${((index + 1) / QUESTION_IDS.length) * 100}%`;

  // Nav buttons
  document.getElementById('btn-prev').disabled = index === 0;
  document.getElementById('btn-next').textContent = index === QUESTION_IDS.length - 1 ? 'Review →' : 'Next →';

  // Show submit on last
  const submitBtn = document.getElementById('btn-submit');
  submitBtn.style.display = index === QUESTION_IDS.length - 1 ? 'block' : 'none';

  updateDots();
}

function selectAnswer(qid, choiceId, btn) {
  answers[qid] = choiceId;
  document.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
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
      time_taken: timeElapsed
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