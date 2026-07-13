document
.getElementById("execute")
.onclick = async function () {

    const message =
        document.getElementById("message").value;

    if(message.trim() === ""){

        alert("Please enter a command.");

        return;
    }

    const responseBox =
        document.getElementById("response");

    responseBox.textContent =
        "🤖 AI is thinking...\n";

    try{

        const response = await fetch(
            "/api/chat",
            {
                method: "POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );

        const data = await response.json();

        responseBox.textContent =
            data.response;

    }catch(err){

        responseBox.textContent =
            "Error : " + err;
    }

}