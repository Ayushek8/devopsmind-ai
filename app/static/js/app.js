const executeButton = document.getElementById("execute");

const messageBox = document.getElementById("message");

const response = document.getElementById("response");

const status = document.getElementById("status");


// ======================================================
// Loading
// ======================================================

function renderLoading() {

    status.innerText = "Thinking...";

    response.innerHTML = `

        <div class="loading">

            🤖 DevOpsMind is investigating...

        </div>

    `;

}


// ======================================================
// Error
// ======================================================

function renderError(message) {

    status.innerText = "Error";

    response.innerHTML = `

        <div class="error">

            ❌ ${message}

        </div>

    `;

}


// ======================================================
// Text
// ======================================================

function renderText(text) {

    status.innerText = "Completed";

    response.innerHTML = `

        <div>

            ${text}

        </div>

    `;

}


// ======================================================
// Workflows
// ======================================================

function renderWorkflows(workflows) {

    status.innerText = "Completed";

    let html = "";

    workflows.forEach(workflow => {

        html += `

        <div class="workflow-card">

            <div class="workflow-name">

                🚀 ${workflow.name}

            </div>

            <div>

                <b>Status</b> :
                ${workflow.state}

            </div>

            <div class="workflow-path">

                ${workflow.path}

            </div>

        </div>

        `;

    });

    response.innerHTML = html;

}

// ======================================================
// Deployment History
// ======================================================

function renderHistory(history) {

    status.innerText = "Completed";

    let html = "";

    history.forEach(run => {

        const color =
            run.conclusion === "success"
                ? "#22c55e"
                : run.conclusion === "failure"
                ? "#ef4444"
                : "#f59e0b";

        html += `

        <div class="workflow-card" style="border-left:5px solid ${color}">

            <div class="workflow-name">

                🚀 ${run.workflow}

            </div>

            <div>

                <b>Branch:</b> ${run.branch}

            </div>

            <div>

                <b>Status:</b> ${run.status}

            </div>

            <div>

                <b>Conclusion:</b> ${run.conclusion}

            </div>

            <div>

                <b>Event:</b> ${run.event}

            </div>

            <div class="workflow-path">

                ${run.created_at}

            </div>

        </div>

        `;

    });

    response.innerHTML = html;
}

// ======================================================
// Incident
// ======================================================

function renderIncident(data) {

    status.innerText = "Completed";

    const incident = data.incident;

    const run = data.run;

    const step = data.step;

    let commands = "";

    if (incident.commands) {

        incident.commands.forEach(cmd => {

            commands += `<div>${cmd}</div>`;

        });

    }

    response.innerHTML = `

<div class="incident-card">

<div class="incident-title">

🚨 ${incident.title}

</div>

<div>

<b>Severity</b>

:

${incident.severity}

</div>

<div class="section">

<div class="section-title">

Workflow

</div>

<div class="section-content">

${run.workflow}

</div>

</div>

<div class="section">

<div class="section-title">

Branch

</div>

<div class="section-content">

${run.branch}

</div>

</div>

<div class="section">

<div class="section-title">

Failed Step

</div>

<div class="section-content">

${step.name}

</div>

</div>

<div class="section">

<div class="section-title">

Root Cause

</div>

<div class="section-content">

${incident.root_cause}

</div>

</div>

<div class="section">

<div class="section-title">

Summary

</div>

<div class="section-content">

${incident.summary}

</div>

</div>

<div class="section">

<div class="section-title">

Suggested Fix

</div>

<div class="section-content">

${incident.fix}

</div>

</div>

<div class="section">

<div class="section-title">

Commands

</div>

<div class="command-box">

${commands}

</div>

</div>

<div class="section">

<div class="section-title">

Confidence

</div>

<div class="section-content">

${incident.confidence}

</div>

</div>

</div>

`;

}

// ======================================================
// Deployment Response
// ======================================================

function renderDeployment(data) {

    status.innerText = "Completed";

    response.innerHTML = `

    <div class="workflow-card">

        <h3>

            ✅ ${data.message}

        </h3>

        <br>

        <div>

            <b>Workflow:</b>

            ${data.workflow}

        </div>

        <div>

            <b>Status:</b>

            ${data.status}

        </div>

        <div>

            <b>Run ID:</b>

            ${data.run_id}

        </div>

    </div>

    `;
}


// ======================================================
// Execute
// ======================================================

executeButton.onclick = async () => {

    const message = messageBox.value.trim();

    if (!message) {

        alert("Please enter a request.");

        return;

    }

    renderLoading();

    try {

        const res = await fetch("/api/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });

        const data = await res.json();

        console.log(data);

        if (!data.success) {

    renderError(

        data.data?.message ||
        data.message ||
        "Unknown Error"

    );

    return;

}


        switch (data.type) {

    case "text":

        renderText(

            data.data

        );

        break;

    case "workflows":

        renderWorkflows(

            data.data

        );

        break;

    case "history":

        renderHistory(

            data.data

        );

        break;

    case "deployment":

        renderDeployment(

            data.data

        );

        break;

    case "incident":

        renderIncident(

            data.data

        );

        break;

    default:

        renderText(

            JSON.stringify(

                data.data,

                null,

                4

            )

        );
            break;
    }         

    }

    catch (err) {

        renderError(

           err.message || err

        );

    }

};