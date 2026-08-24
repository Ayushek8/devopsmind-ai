// ======================================================
// TalkOps Chat Components (Revamped Messaging Bubbles UI)
// ======================================================
const executeButton = document.getElementById("execute");
const messageBox = document.getElementById("message");
const chatBubbles = document.getElementById("chat-bubbles");
const responseContainer = document.getElementById("response-container");
const statusText = document.getElementById("status");

let typingIndicator = null;

function showTypingIndicator() {
    statusText.innerText = "Thinking...";
    statusText.className = "status-badge thinking";
    
    typingIndicator = document.createElement("div");
    typingIndicator.className = "chat-bubble ai typing";
    typingIndicator.innerHTML = `
        <div class="bubble-avatar">🤖</div>
        <div class="bubble-body">
            <div class="bubble-sender">DevOpsMind</div>
            <div class="bubble-content">
                <div class="typing-indicator">
                    <span></span><span></span><span></span>
                </div>
            </div>
        </div>
    `;
    chatBubbles.appendChild(typingIndicator);
    responseContainer.scrollTop = responseContainer.scrollHeight;
}

function removeTypingIndicator() {
    if (typingIndicator) {
        typingIndicator.remove();
        typingIndicator = null;
    }
}

function appendChatBubble(sender, contentHTML, isError = false) {
    if (!chatBubbles) return;
    const bubble = document.createElement("div");
    bubble.className = `chat-bubble ${sender} ${isError ? 'error-bubble' : ''}`;
    
    const avatar = sender === 'user' ? '👤' : '🤖';
    const senderName = sender === 'user' ? 'You' : 'DevOpsMind';
    
    bubble.innerHTML = `
        <div class="bubble-avatar">${avatar}</div>
        <div class="bubble-body">
            <div class="bubble-sender">${senderName}</div>
            <div class="bubble-content">${contentHTML}</div>
        </div>
    `;
    
    chatBubbles.appendChild(bubble);
    responseContainer.scrollTop = responseContainer.scrollHeight;
}

function renderError(message) {
    statusText.innerText = "Error";
    statusText.className = "status-badge error";
    appendChatBubble("ai", `❌ ${message}`, true);
}

function renderText(text) {
    statusText.innerText = "Completed";
    statusText.className = "status-badge completed";
    appendChatBubble("ai", `<div>${text}</div>`);
}

function renderWorkflows(workflows) {
    statusText.innerText = "Completed";
    statusText.className = "status-badge completed";
    let html = "<div style='display:flex; flex-direction:column; gap:12px;'>";
    workflows.forEach((workflow) => {
        html += `
        <div class="workflow-card">
            <div class="workflow-name">🚀 ${workflow.name}</div>
            <div><b>Status</b>: ${workflow.state}</div>
            <div class="workflow-path">${workflow.path}</div>
        </div>
        `;
    });
    html += "</div>";
    appendChatBubble("ai", html);
}

function renderHistory(history) {
    statusText.innerText = "Completed";
    statusText.className = "status-badge completed";
    let html = "<div style='display:flex; flex-direction:column; gap:12px;'>";
    history.forEach((run) => {
        const color =
            run.conclusion === "success"
                ? "#22c55e"
                : run.conclusion === "failure"
                ? "#ef4444"
                : "#f59e0b";

        html += `
        <div class="workflow-card" style="border-left:5px solid ${color}">
            <div class="workflow-name">🚀 ${run.workflow}</div>
            <div><b>Branch:</b> ${run.branch}</div>
            <div><b>Status:</b> ${run.status}</div>
            <div><b>Conclusion:</b> ${run.conclusion}</div>
            <div><b>Event:</b> ${run.event}</div>
            <div class="workflow-path">${run.created_at}</div>
        </div>
        `;
    });
    html += "</div>";
    appendChatBubble("ai", html);
}

function renderIncident(data) {
    statusText.innerText = "Completed";
    statusText.className = "status-badge completed";
    const incident = data.incident;
    const run = data.run;
    const step = data.step;

    const severity = (incident.severity || "info").toLowerCase();
    const severityIcon = {
        critical: "🔴",
        high: "🟠",
        medium: "🟡",
        low: "🟢",
        error: "🔴",
        warning: "🟠",
        info: "🔵",
    };
    const severityText = severity.charAt(0).toUpperCase() + severity.slice(1);

    let commands = "";
    if (Array.isArray(incident.commands) && incident.commands.length > 0) {
        commands = incident.commands
            .map((cmd) => `
                <div style="display:flex; justify-content:space-between; align-items:center; background:#000; padding:10px; border-radius:6px; margin-bottom:8px; font-family:monospace; color:#22c55e;">
                    <span>$ ${cmd}</span>
                    <button onclick="navigator.clipboard.writeText('${cmd}'); alert('Copied to clipboard!');" style="margin-top:0; padding:4px 8px; font-size:11px; background:#334155;">Copy</button>
                </div>
            `)
            .join("");
    } else {
        commands = `<div>No recommended commands.</div>`;
    }

    const confidence = Math.round(
        Number(incident.confidence) <= 1
            ? Number(incident.confidence) * 100
            : Number(incident.confidence)
    );

    const html = `
        <div class="incident-card">
            <div class="incident-title">🚨 ${incident.title}</div>
            <div>
                <b>Severity:</b>
                <span style="color:#f59e0b;font-weight:bold">
                    ${severityIcon[severity] || "⚪"} ${severityText}
                </span>
            </div>
            <div class="section">
                <div class="section-title">Workflow</div>
                <div class="section-content">${run.workflow}</div>
            </div>
            <div class="section">
                <div class="section-title">Branch</div>
                <div class="section-content">${run.branch}</div>
            </div>
            <div class="section">
                <div class="section-title">Failed Step</div>
                <div class="section-content">${step.name}</div>
            </div>
            <div class="section">
                <div class="section-title">Root Cause</div>
                <div class="section-content">${incident.root_cause}</div>
            </div>
            <div class="section">
                <div class="section-title">Summary</div>
                <div class="section-content">${incident.summary}</div>
            </div>
            <div class="section">
                <div class="section-title">Suggested Fix</div>
                <div class="section-content">${incident.fix}</div>
            </div>
            <div class="section">
                <div class="section-title">Commands</div>
                <div style="margin-top:10px;">${commands}</div>
            </div>
            <div class="section" style="margin-top:20px; border-top:1px dashed var(--border); padding-top:12px;">
                <span style="font-size:12px; color:var(--muted)">Agent Confidence: ${confidence}%</span>
            </div>
        </div>
    `;
    appendChatBubble("ai", html);
}

function renderDeployment(data) {
    statusText.innerText = "Completed";
    statusText.className = "status-badge completed";
    const html = `
        <div class="workflow-card">
            <h3>✅ ${data.message}</h3>
            <br>
            <div><b>Workflow:</b> ${data.workflow}</div>
            <div><b>Status:</b> ${data.status}</div>
            <div><b>Run ID:</b> ${data.run_id}</div>
        </div>
    `;
    appendChatBubble("ai", html);
}

if (executeButton) {
    executeButton.onclick = async () => {
        const message = messageBox.value.trim();
        if (!message) {
            alert("Please enter a request.");
            return;
        }
        
        appendChatBubble("user", `<div>${message}</div>`);
        messageBox.value = "";
        
        showTypingIndicator();
        try {
            const res = await fetch("/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message }),
            });
            const data = await res.json();
            
            removeTypingIndicator();
            
            if (!data.success) {
                renderError(data.data?.message || data.message || "Unknown Error");
                return;
            }
            switch (data.type) {
                case "text":
                    renderText(data.data);
                    break;
                case "workflows":
                    renderWorkflows(data.data);
                    break;
                case "history":
                    renderHistory(data.data);
                    break;
                case "deployment":
                    renderDeployment(data.data);
                    break;
                case "incident":
                    renderIncident(data.data);
                    break;
                default:
                    renderText(JSON.stringify(data.data, null, 4));
                    break;
            }
        } catch (err) {
            removeTypingIndicator();
            renderError(err.message || err);
        }
    };
}

// Quick suggestions wiring
document.querySelectorAll(".suggest-btn").forEach(btn => {
    btn.onclick = () => {
        messageBox.value = btn.dataset.prompt;
        executeButton.click();
    };
});


// ======================================================
// Dashboard Tab Switching & State Management
// ======================================================
let selectedWorkflow = null;
let selectedRunId = null;

const tabChat = document.getElementById("tab-chat");
const tabDashboard = document.getElementById("tab-dashboard");
const contentChat = document.getElementById("content-chat");
const contentDashboard = document.getElementById("content-dashboard");

if (tabChat && tabDashboard) {
    tabChat.onclick = () => {
        tabChat.classList.add("active");
        tabDashboard.classList.remove("active");
        contentChat.classList.add("active");
        contentDashboard.classList.remove("active");
    };

    tabDashboard.onclick = () => {
        tabDashboard.classList.add("active");
        tabChat.classList.remove("active");
        contentDashboard.classList.add("active");
        contentChat.classList.remove("active");
        
        // Initial load of dashboard content
        loadWorkflows();
        loadRuns();
    };
}


// ======================================================
// Workflows & Runs Handlers
// ======================================================
const workflowsList = document.getElementById("workflows-list");
const runsList = document.getElementById("runs-list");
const currentWorkflowTitle = document.getElementById("current-workflow-title");
const btnTriggerRun = document.getElementById("btn-trigger-run");
const btnRefreshWorkflows = document.getElementById("btn-refresh-workflows");
const btnRefreshRuns = document.getElementById("btn-refresh-runs");

let allWorkflows = [];
let allLoadedRuns = [];

async function loadWorkflows() {
    workflowsList.innerHTML = `<div class="loading-small">Loading workflows...</div>`;
    try {
        const res = await fetch("/api/github/workflows");
        const data = await res.json();
        if (!data.success) {
            workflowsList.innerHTML = `<div class="error">Failed to load workflows: ${data.error}</div>`;
            return;
        }

        allWorkflows = data.workflows || [];
        renderWorkflowsList();
    } catch (err) {
        workflowsList.innerHTML = `<div class="error">Error: ${err.message}</div>`;
    }
}

function renderWorkflowsList() {
    const searchVal = document.getElementById("workflow-search")?.value.toLowerCase().trim() || "";
    
    let filteredWorkflows = allWorkflows;
    if (searchVal) {
        filteredWorkflows = allWorkflows.filter(wf => wf.name.toLowerCase().includes(searchVal) || wf.path.toLowerCase().includes(searchVal));
    }
    
    let html = `
        <div class="workflow-item ${!selectedWorkflow ? 'active' : ''}" id="wf-all">
            <h4>All Workflows</h4>
            <span>Show recent runs across repo</span>
        </div>
    `;

    filteredWorkflows.forEach(wf => {
        const isActive = selectedWorkflow && selectedWorkflow.path === wf.path;
        const filename = wf.path.split("/").pop();
        html += `
            <div class="workflow-item ${isActive ? 'active' : ''}" data-path="${wf.path}" data-name="${wf.name}" data-filename="${filename}">
                <h4>🚀 ${wf.name}</h4>
                <span>${filename} | ${wf.state}</span>
            </div>
        `;
    });
    workflowsList.innerHTML = html;

    // Add event listeners
    document.querySelectorAll(".workflow-item").forEach(item => {
        item.onclick = () => {
            document.querySelectorAll(".workflow-item").forEach(el => el.classList.remove("active"));
            item.classList.add("active");

            if (item.id === "wf-all") {
                selectedWorkflow = null;
                currentWorkflowTitle.innerText = "All Recent Runs";
                btnTriggerRun.classList.add("disabled");
                btnTriggerRun.disabled = true;
                loadRuns();
            } else {
                selectedWorkflow = {
                    path: item.dataset.path,
                    name: item.dataset.name,
                    filename: item.dataset.filename
                };
                currentWorkflowTitle.innerText = `Runs: ${selectedWorkflow.name}`;
                btnTriggerRun.classList.remove("disabled");
                btnTriggerRun.disabled = false;
                loadRuns(selectedWorkflow.filename);
            }
        };
    });
}

// Bind search input
const workflowSearch = document.getElementById("workflow-search");
if (workflowSearch) {
    workflowSearch.oninput = () => {
        renderWorkflowsList();
    };
}

async function loadRuns(workflowFile = null) {
    runsList.innerHTML = `<div class="loading-small">Loading runs...</div>`;
    try {
        const url = workflowFile ? `/api/github/runs?workflow_file=${workflowFile}` : `/api/github/runs`;
        const res = await fetch(url);
        const data = await res.json();
        if (!data.success) {
            runsList.innerHTML = `<div class="error">Failed to load runs: ${data.error}</div>`;
            return;
        }

        allLoadedRuns = data.runs || [];
        updateDashboardStats(allLoadedRuns);
        renderRunsList();
    } catch (err) {
        runsList.innerHTML = `<div class="error">Error: ${err.message}</div>`;
    }
}

function renderRunsList() {
    const statusFilter = document.getElementById("run-status-filter")?.value || "all";
    
    let filteredRuns = allLoadedRuns;
    if (statusFilter !== "all") {
        if (statusFilter === "in_progress" || statusFilter === "queued") {
            filteredRuns = allLoadedRuns.filter(r => r.status === statusFilter);
        } else {
            // success, failure, cancelled
            filteredRuns = allLoadedRuns.filter(r => r.status === "completed" && r.conclusion === statusFilter);
        }
    }
    
    if (filteredRuns.length === 0) {
        runsList.innerHTML = `<div class="loading-small">No runs matching filter.</div>`;
        return;
    }

    let html = "";
    filteredRuns.forEach(run => {
        const statusClass = `status-${run.status === "completed" ? (run.conclusion || "queued") : run.status}`;
        const createdDate = new Date(run.created_at).toLocaleString();
        
        html += `
            <div class="run-card-item" data-run-id="${run.id}">
                <div class="run-left">
                    <div class="run-status-indicator ${statusClass}"></div>
                    <div class="run-info">
                        <h4>${run.workflow} <span class="run-meta">#${run.id}</span></h4>
                        <p><strong>Branch:</strong> ${run.branch} | <strong>Event:</strong> ${run.event}</p>
                        <p class="commit-msg">Commit: ${run.commit_message}</p>
                    </div>
                </div>
                <div class="run-right">
                    <span class="run-time">${createdDate}</span>
                    <a href="${run.url}" target="_blank" class="run-meta" style="color:var(--blue);text-decoration:none;" onclick="event.stopPropagation();">View on GitHub ↗</a>
                </div>
            </div>
        `;
    });
    runsList.innerHTML = html;

    // Add event listeners to run cards to open details drawer
    document.querySelectorAll(".run-card-item").forEach(card => {
        card.onclick = () => {
            const runId = card.dataset.runId;
            openRunDrawer(runId);
        };
    });
}

// Bind status filter dropdown
const runStatusFilter = document.getElementById("run-status-filter");
if (runStatusFilter) {
    runStatusFilter.onchange = () => {
        renderRunsList();
    };
}

// Computes dynamic statistics from runs
function updateDashboardStats(runs) {
    if (!runs) return;
    
    const totalRuns = runs.length;
    
    const completedRuns = runs.filter(r => r.status === "completed" && (r.conclusion === "success" || r.conclusion === "failure"));
    const successRuns = completedRuns.filter(r => r.conclusion === "success");
    const failedRuns = runs.filter(r => r.conclusion === "failure");
    const activeRuns = runs.filter(r => r.status !== "completed");
    
    const successRate = completedRuns.length > 0 
        ? Math.round((successRuns.length / completedRuns.length) * 100) 
        : 100;
        
    const totalEl = document.getElementById("stat-total-runs");
    const rateEl = document.getElementById("stat-success-rate");
    const failedEl = document.getElementById("stat-failed-runs");
    const activeEl = document.getElementById("stat-active-runs");
    
    if (totalEl) totalEl.innerText = totalRuns;
    if (rateEl) rateEl.innerText = `${successRate}%`;
    if (failedEl) failedEl.innerText = failedRuns.length;
    if (activeEl) activeEl.innerText = activeRuns.length;
}

if (btnRefreshWorkflows) {
    btnRefreshWorkflows.onclick = () => loadWorkflows();
}

if (btnRefreshRuns) {
    btnRefreshRuns.onclick = () => {
        loadRuns(selectedWorkflow ? selectedWorkflow.filename : null);
    };
}


// ======================================================
// Run Details Drawer Handlers
// ======================================================
const runDetailPanel = document.getElementById("run-detail-panel");
const drawerRunTitle = document.getElementById("drawer-run-title");
const drawerRunBadge = document.getElementById("drawer-run-badge");
const runDetailBranch = document.getElementById("run-detail-branch");
const runDetailEvent = document.getElementById("run-detail-event");
const runDetailCommit = document.getElementById("run-detail-commit");
const drawerClose = document.getElementById("drawer-close");

const btnRetryRun = document.getElementById("btn-retry-run");
const btnCancelRun = document.getElementById("btn-cancel-run");
const btnAiInvestigate = document.getElementById("btn-ai-investigate");

const jobsContainer = document.getElementById("jobs-container");
const logTabRaw = document.getElementById("log-tab-raw");
const logTabAi = document.getElementById("log-tab-ai");
const logViewerConsole = document.getElementById("log-viewer-console");
const logViewerAi = document.getElementById("log-viewer-ai");

async function openRunDrawer(runId) {
    selectedRunId = runId;
    runDetailPanel.classList.add("open");
    
    // Set loading state in detail elements
    drawerRunTitle.innerText = `Run #${runId}`;
    drawerRunBadge.className = "run-status-badge queued";
    drawerRunBadge.innerText = "loading...";
    jobsContainer.innerHTML = `<div class="loading-small">Loading jobs...</div>`;
    logViewerConsole.innerText = "Select a step to view console logs.";
    logViewerAi.innerText = "Select a failed run and click 'AI SRE Investigate' to generate failure diagnostics.";

    // Default tabs state
    showLogTab("raw");

    try {
        // Fetch run details
        const runRes = await fetch(`/api/github/runs/${runId}`);
        const runData = await runRes.json();
        if (runData.success) {
            const run = runData.run;
            drawerRunTitle.innerText = `${run.name || "Workflow"} #${run.id}`;
            const conclusion = run.conclusion || run.status;
            drawerRunBadge.className = `run-status-badge ${conclusion}`;
            drawerRunBadge.innerText = conclusion;
            runDetailBranch.innerText = run.head_branch;
            runDetailEvent.innerText = run.event;
            runDetailCommit.innerText = run.head_commit?.message || "N/A";

            // Enable/disable action buttons
            if (run.status === "completed") {
                btnCancelRun.disabled = true;
                btnRetryRun.disabled = false;
            } else {
                btnCancelRun.disabled = false;
                btnRetryRun.disabled = true;
            }

            if (run.conclusion === "failure") {
                btnAiInvestigate.disabled = false;
            } else {
                btnAiInvestigate.disabled = true;
            }
        }

        // Fetch jobs & steps
        const jobsRes = await fetch(`/api/github/runs/${runId}/jobs`);
        const jobsData = await jobsRes.json();
        if (!jobsData.success) {
            jobsContainer.innerHTML = `<div class="error">Failed to load jobs</div>`;
            return;
        }

        let jobsHtml = "";
        jobsData.jobs.forEach(job => {
            jobsHtml += `
                <div class="job-item">
                    <div class="job-title">
                        🏢 ${job.name} (${job.conclusion || job.status})
                    </div>
                    <div class="steps-list">
            `;
            job.steps.forEach(step => {
                const stepStatusIcon = step.conclusion === "success" ? "✅" : step.conclusion === "failure" ? "❌" : step.status === "in_progress" ? "⏳" : "⚪";
                jobsHtml += `
                    <div class="step-item" data-job-id="${job.id}" data-step-name="${step.name}">
                        <span>${stepStatusIcon} ${step.name}</span>
                        <span class="icon">📄</span>
                    </div>
                `;
            });
            jobsHtml += `
                    </div>
                </div>
            `;
        });
        jobsContainer.innerHTML = jobsHtml;

        // Add event listener to step items to load logs
        document.querySelectorAll(".step-item").forEach(step => {
            step.onclick = () => {
                document.querySelectorAll(".step-item").forEach(el => el.classList.remove("active"));
                step.classList.add("active");
                
                const jobId = step.dataset.jobId;
                const stepName = step.dataset.stepName;
                loadStepLogs(runId, jobId, stepName);
            };
        });

    } catch (err) {
        jobsContainer.innerHTML = `<div class="error">Error loading details: ${err.message}</div>`;
    }
}

async function loadStepLogs(runId, jobId, stepName) {
    logViewerConsole.innerText = `Fetching logs for step "${stepName}"...`;
    showLogTab("raw");
    try {
        const res = await fetch(`/api/github/runs/${runId}/jobs/${jobId}/logs`);
        const data = await res.json();
        if (!data.success) {
            logViewerConsole.innerText = `Failed to retrieve logs: ${data.error}`;
            return;
        }

        // Github step logs are split by group markers or timestamps. 
        // We will display the log section belonging to the specific step if we find the matching step header.
        const rawLogs = data.logs;
        const lines = rawLogs.split('\n');
        
        // Find step log bounds
        let stepLogs = [];
        let capturing = false;
        
        // Match timestamps followed by step names, e.g., "2026-08-12T05:00:00.000Z ##[group]Run actions/checkout@v4"
        const groupStartRegex = new RegExp(`##\\[group\\](?:Run\\s+)?${escapeRegExp(stepName)}`, 'i');
        const stepStartRegex = new RegExp(`##\\[group\\](?:Run\\s+)?${escapeRegExp(stepName)}|Starting:\\s+${escapeRegExp(stepName)}`, 'i');
        
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            
            // Check for step start
            if (!capturing && (stepStartRegex.test(line) || line.toLowerCase().includes(`run ${stepName.toLowerCase()}`))) {
                capturing = true;
                stepLogs.push(line);
                continue;
            }
            
            // If capturing, append lines until next group or job end
            if (capturing) {
                // If it is another group marker, stop capturing
                if (line.includes("##[group]") && !line.includes(stepName)) {
                    break;
                }
                stepLogs.push(line);
            }
        }

        if (stepLogs.length > 0) {
            logViewerConsole.innerText = stepLogs.join('\n');
        } else {
            // Fallback: render the last 500 lines of the job logs if step-specific bounds aren't parsed
            logViewerConsole.innerText = `--- Full Job Logs (Step bounds not parsed) ---\n\n` + rawLogs;
        }
    } catch (err) {
        logViewerConsole.innerText = `Error: ${err.message}`;
    }
}

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function showLogTab(tab) {
    if (tab === "raw") {
        logTabRaw.classList.add("active");
        logTabAi.classList.remove("active");
        logViewerConsole.classList.add("active");
        logViewerAi.classList.remove("active");
    } else {
        logTabAi.classList.add("active");
        logTabRaw.classList.remove("active");
        logViewerAi.classList.add("active");
        logViewerConsole.classList.remove("active");
    }
}

if (logTabRaw && logTabAi) {
    logTabRaw.onclick = () => showLogTab("raw");
    logTabAi.onclick = () => showLogTab("ai");
}

if (drawerClose) {
    drawerClose.onclick = () => {
        runDetailPanel.classList.remove("open");
        selectedRunId = null;
    };
}


// ======================================================
// Actions Drawer Buttons (Cancel / Rerun / Investigate)
// ======================================================
if (btnCancelRun) {
    btnCancelRun.onclick = async () => {
        if (!selectedRunId) return;
        if (!confirm("Are you sure you want to cancel this run?")) return;
        
        btnCancelRun.disabled = true;
        btnCancelRun.innerText = "Cancelling...";
        
        try {
            const res = await fetch(`/api/github/runs/${selectedRunId}/cancel`, { method: "POST" });
            const data = await res.json();
            if (data.success) {
                alert("Workflow run cancellation requested.");
                openRunDrawer(selectedRunId);
                loadRuns(selectedWorkflow ? selectedWorkflow.filename : null);
            } else {
                alert(`Cancel failed: ${data.error}`);
                btnCancelRun.disabled = false;
                btnCancelRun.innerText = "🚫 Cancel Run";
            }
        } catch (err) {
            alert(`Error: ${err.message}`);
            btnCancelRun.disabled = false;
            btnCancelRun.innerText = "🚫 Cancel Run";
        }
    };
}

if (btnRetryRun) {
    btnRetryRun.onclick = async () => {
        if (!selectedRunId) return;
        if (!confirm("Are you sure you want to rerun jobs in this run?")) return;
        
        btnRetryRun.disabled = true;
        btnRetryRun.innerText = "Re-running...";
        
        try {
            const res = await fetch(`/api/github/runs/${selectedRunId}/retry`, { method: "POST" });
            const data = await res.json();
            if (data.success) {
                alert("Workflow rerun dispatch successfully requested.");
                openRunDrawer(selectedRunId);
                loadRuns(selectedWorkflow ? selectedWorkflow.filename : null);
            } else {
                alert(`Rerun failed: ${data.error}`);
                btnRetryRun.disabled = false;
                btnRetryRun.innerText = "🔄 Rerun Jobs";
            }
        } catch (err) {
            alert(`Error: ${err.message}`);
            btnRetryRun.disabled = false;
            btnRetryRun.innerText = "🔄 Rerun Jobs";
        }
    };
}

if (btnAiInvestigate) {
    btnAiInvestigate.onclick = async () => {
        if (!selectedRunId) return;
        showLogTab("ai");
        logViewerAi.innerHTML = `
            <div class="loading">
                🤖 AI SRE agent is downloading logs and analyzing build failure...
            </div>
        `;
        
        try {
            const res = await fetch(`/api/github/runs/${selectedRunId}/investigate`, { method: "POST" });
            const data = await res.json();
            if (!data.success) {
                logViewerAi.innerHTML = `<div class="error">AI SRE Agent investigation failed: ${data.error}</div>`;
                return;
            }
            
            const incident = data.data.incident;
            const run = data.data.run;
            const step = data.data.step;
            
            const confidence = Math.round(
                Number(incident.confidence) <= 1
                    ? Number(incident.confidence) * 100
                    : Number(incident.confidence)
            );
            
            const severity = (incident.severity || "info").toLowerCase();
            const severityColors = {
                critical: "#ef4444",
                high: "#f59e0b",
                medium: "#f59e0b",
                low: "#22c55e",
                warning: "#f59e0b",
                error: "#ef4444"
            };
            const color = severityColors[severity] || "#94a3b8";
            
            let commandsHtml = "";
            if (Array.isArray(incident.commands) && incident.commands.length > 0) {
                incident.commands.forEach(cmd => {
                    commandsHtml += `
                        <div style="display:flex; justify-content:space-between; align-items:center; background:#000; padding:10px; border-radius:6px; margin-bottom:8px; font-family:monospace; color:#22c55e;">
                            <span>$ ${cmd}</span>
                            <button onclick="navigator.clipboard.writeText('${cmd}'); alert('Copied to clipboard!');" style="margin-top:0; padding:4px 8px; font-size:11px; background:#334155;">Copy</button>
                        </div>
                    `;
                });
            } else {
                commandsHtml = `<div>No recommended commands.</div>`;
            }

            logViewerAi.innerHTML = `
                <div class="incident-card" style="border-left: 5px solid ${color}">
                    <h3 class="incident-title">🚨 ${incident.title}</h3>
                    
                    <div class="section">
                        <div class="section-title">Severity</div>
                        <div class="section-content">
                            <span class="badge" style="background:${color}; color:#000; font-weight:bold;">
                                ${incident.severity.toUpperCase()}
                            </span>
                        </div>
                    </div>
                    
                    <div class="section">
                        <div class="section-title">Failed Step</div>
                        <div class="section-content">
                            <strong>Job:</strong> ${data.data.job?.name || "N/A"} | <strong>Step:</strong> ${step.name}
                        </div>
                    </div>
                    
                    <div class="section">
                        <div class="section-title">Root Cause Analysis</div>
                        <div class="section-content">${incident.root_cause}</div>
                    </div>
                    
                    <div class="section">
                        <div class="section-title">Summary</div>
                        <div class="section-content">${incident.summary}</div>
                    </div>
                    
                    <div class="section">
                        <div class="section-title">Suggested Remediation</div>
                        <div class="section-content">${incident.fix}</div>
                    </div>
                    
                    <div class="section">
                        <div class="section-title">Recommended Diagnostics / Commands</div>
                        <div style="margin-top:10px;">${commandsHtml}</div>
                    </div>
                    
                    <div class="section" style="margin-top:20px; border-top:1px dashed var(--border); padding-top:12px;">
                        <span style="font-size:12px; color:var(--muted)">Agent Confidence: ${confidence}%</span>
                    </div>
                </div>
            `;
        } catch (err) {
            logViewerAi.innerHTML = `<div class="error">Error querying SRE agent: ${err.message}</div>`;
        }
    };
}


// ======================================================
// Trigger Workflow Modal Handlers
// ======================================================
const modalTrigger = document.getElementById("modal-trigger");
const triggerForm = document.getElementById("trigger-form");
const triggerWorkflowFile = document.getElementById("trigger-workflow-file");
const triggerBranch = document.getElementById("trigger-branch");
const triggerInputs = document.getElementById("trigger-inputs");
const modalClose = document.getElementById("modal-close");

if (btnTriggerRun) {
    btnTriggerRun.onclick = () => {
        if (!selectedWorkflow) return;
        triggerWorkflowFile.value = selectedWorkflow.filename;
        triggerBranch.value = "main";
        triggerInputs.value = "";
        modalTrigger.classList.add("open");
    };
}

if (modalClose) {
    modalClose.onclick = () => {
        modalTrigger.classList.remove("open");
    };
}

// Close modal when clicking outside contents
window.onclick = (e) => {
    if (e.target === modalTrigger) {
        modalTrigger.classList.remove("open");
    }
};

if (triggerForm) {
    triggerForm.onsubmit = async (e) => {
        e.preventDefault();
        
        const workflowFile = triggerWorkflowFile.value;
        const ref = triggerBranch.value.trim();
        let inputs = null;

        if (triggerInputs.value.trim()) {
            try {
                inputs = JSON.parse(triggerInputs.value.trim());
            } catch (err) {
                alert(`Invalid JSON format in inputs field: ${err.message}`);
                return;
            }
        }

        const submitBtn = triggerForm.querySelector("button[type='submit']");
        submitBtn.disabled = true;
        submitBtn.innerText = "Dispatching...";

        try {
            const res = await fetch(`/api/github/workflows/${workflowFile}/trigger`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ ref, inputs }),
            });
            const data = await res.json();
            if (data.success) {
                alert(`Workflow run dispatched successfully!`);
                modalTrigger.classList.remove("open");
                loadRuns(workflowFile);
            } else {
                alert(`Failed to trigger workflow: ${data.error}`);
            }
        } catch (err) {
            alert(`Error triggering workflow: ${err.message}`);
        } finally {
            submitBtn.disabled = false;
            submitBtn.innerText = "⚡ Dispatch Run";
        }
    };
}
