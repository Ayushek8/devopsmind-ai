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

                data.data.message

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

        }

    }

    catch (err) {

        renderError(

            err

        );

    }

};