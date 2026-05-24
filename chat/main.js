const chatBox = document.getElementById("chatBox");
const input = document.getElementById("input");

function addUserMessage(text) {
    const div = document.createElement("div");
    div.className = "user-msg";
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addBotMessage(text) {
    const div = document.createElement("div");
    div.className = "bot-msg";
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const userMessage = input.value.trim();
    if (!userMessage) return;

    addUserMessage(userMessage);
    input.value = "";

    addBotMessage("Thinking...");
    const botNode = chatBox.lastChild;

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: userMessage
            })
        });

        const data = await res.json();
        botNode.innerText = data.response;

    } catch (err) {
        botNode.innerText = "Server error.";
    }
}

input.addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});