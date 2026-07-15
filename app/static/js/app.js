document
.getElementById("execute")
.onclick = async function () {

    const message =
        document.getElementById("message").value;

    if (message.trim() === "") {

        alert("Please enter a command.");

        return;

    }

    const responseBox =
        document.getElementById("response");

    responseBox.textContent =
        "🤖 AI is thinking...";

    try {

        const response = await fetch(

            "/api/chat",

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    message: message

                })

            }

        );

        const text = await response.text();

        let data;

        try {

            data = JSON.parse(text);

        }

        catch {

            responseBox.textContent = text;

            return;

        }

        if (!data.success) {

            responseBox.textContent =
                data.response;

            return;

        }

        // ------------------------------------
        // TEXT
        // ------------------------------------

        if (data.type === "text") {

            responseBox.textContent =
                data.response;

            return;

        }

        // ------------------------------------
        // WORKFLOWS
        // ------------------------------------

        if (data.type === "workflows") {

            let output = "";

            output +=
                "📋 GitHub Workflows\n\n";

            data.response.forEach(workflow => {

                output +=
`Name   : ${workflow.name}
State  : ${workflow.state}
Path   : ${workflow.path}

--------------------------------------------

`;

            });

            responseBox.textContent =
                output;

            return;

        }

        // ------------------------------------
        // DEPLOYMENT STATUS
        // ------------------------------------

        if (data.type === "deployment_status") {

            const d = data.response;

            responseBox.textContent =

`🚀 Deployment Status

Workflow   : ${d.workflow}

Branch     : ${d.branch}

Status     : ${d.status}

Conclusion : ${d.conclusion}

Event      : ${d.event}

Run ID     : ${d.run_id}

URL

${d.url}`;

            return;

        }

        responseBox.textContent =
            JSON.stringify(
                data.response,
                null,
                4
            );

    }

    catch (err) {

        responseBox.textContent =
            err;

    }

}