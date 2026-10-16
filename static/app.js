let lastAdvice = "";
let lastAdviceTime = 0; // ⏱️ controls UI lock (NOT API)
let lastAPICallTime = 0; // 🔥 NEW: controls API calls

/* =========================
   MAIN METRICS FUNCTION
========================= */
async function fetchMetrics() {
    try {
        const res = await fetch("/metrics");
        const data = await res.json();

        const stressEl = document.getElementById("stress");

        // =========================
        // Basic Values
        // =========================
        stressEl.innerText = data.stress ?? 0;
        // document.getElementById("emotion").innerText = data.emotion ?? "neutral";
        document.getElementById("mouse").innerText = data.mouse_clicks ?? 0;
        document.getElementById("keyboard").innerText = data.key_strokes ?? 0;
        document.getElementById("blinks").innerText = data.blinks ?? 0;

        // =========================
        // Posture (with color)
        // =========================
        const postureEl = document.getElementById("posture");
        postureEl.innerText = data.posture ?? "Good";

        if (data.posture === "Good") {
            postureEl.style.color = "#22c55e";
        } else {
            postureEl.style.color = "#ef4444";
        }

        // =========================
        // Screen Time (HH:MM:SS)
        // =========================
        let seconds = data.screen_time ?? 0;

        let hrs = Math.floor(seconds / 3600);
        let mins = Math.floor((seconds % 3600) / 60);
        let secs = Math.floor(seconds % 60);

        document.getElementById("screen").innerText =
            `${hrs.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

        // =========================
        // Stress Color
        // =========================
        stressEl.className = "value";

        if (data.stress < 40) {
            stressEl.classList.add("stress-low");
        } else if (data.stress < 70) {
            stressEl.classList.add("stress-mid");
        } else {
            stressEl.classList.add("stress-high");
        }

        // =========================
        // Alerts Logic
        // =========================
        const alertBox = document.getElementById("alert");

        if (data.stress > 70) {
            alertBox.innerText = "⚠ High stress detected. Take a break!";
            alertBox.classList.remove("hidden");
        } else if (data.posture !== "Good") {
            alertBox.innerText = "⚠ Fix your posture!";
            alertBox.classList.remove("hidden");
        } else if (seconds > 1800) {
            alertBox.innerText = "⚠ You've been working too long. Take rest!";
            alertBox.classList.remove("hidden");
        } else {
            alertBox.classList.add("hidden");
        }

        // =========================
        // 🔥 AI CALL (RATE LIMITED)
        // =========================
        const now = Date.now();

        // 👉 call AI only once in 15 sec
        if (now - lastAPICallTime > 15000) {
            lastAPICallTime = now;
            fetchAIAdvice(data.stress);
        }

    } catch (err) {
        console.error("Error fetching metrics:", err);
    }
}

setInterval(fetchMetrics, 1000);
fetchMetrics();


/* =========================
   GEMINI AI (UI LOCK 15s)
========================= */
async function fetchAIAdvice(stress) {
    const adviceBox = document.getElementById("ai-advice");
    const now = Date.now();

    try {
        // ✅ LOW STRESS → RESET
        if (stress <= 50) {
            adviceBox.innerText = "All good ";
            lastAdvice = "";
            lastAdviceTime = 0;
            return;
        }

        // ✅ API CALL (now limited)
        const res = await fetch("/ai_recommendation");
        const data = await res.json();

        const newAdvice = data.advice ?? "Stay healthy!";

        // ⛔ UI LOCK → DO NOT UPDATE FOR 15 SEC
        if (now - lastAdviceTime < 15000) {
            return;
        }

        // ✅ UPDATE UI AFTER 15 SEC
        if (newAdvice !== lastAdvice) {
            adviceBox.innerText = newAdvice;
            lastAdvice = newAdvice;
            lastAdviceTime = now;
        }

    } catch (err) {
        console.error("AI error:", err);
    }
}
// SWITCH BETWEEN SECTIONS
function showSection(section) {
    document.getElementById("dashboard-section").classList.add("hidden");
    document.getElementById("tasks-section").classList.add("hidden");

    if (section === "dashboard") {
        document.getElementById("dashboard-section").classList.remove("hidden");
    } else {
        document.getElementById("tasks-section").classList.remove("hidden");
    }
}

// ADD TASK
function addTask() {
    const input = document.getElementById("task-input");
    const taskText = input.value.trim();

    if (taskText === "") return;

    const li = document.createElement("li");
    li.textContent = taskText;

    // click to remove task
    li.onclick = () => li.remove();

    document.getElementById("task-list").appendChild(li);

    input.value = "";
}
