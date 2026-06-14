let chatHistory = JSON.parse(localStorage.getItem("chatHistory")) || [];
//// added localStorage to save chat history and load it on page refresh


const chatBox = document.getElementById("chatBox");
const input = document.getElementById("input");

function saveHistory() {
    localStorage.setItem("chatHistory", JSON.stringify(chatHistory));
}

function addUserMessage(text) {
    const div = document.createElement("div");

    div.className = "user-msg";
    div.innerText = text;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

    chatHistory.push({
        role: "user",
        text: text
    });

    saveHistory();
}

function addBotMessage(text) {
    const div = document.createElement("div");

    div.className = "bot-msg";
    div.innerText = text;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

    return div;
}

function loadChatHistory() {
    chatBox.innerHTML = "";

    chatHistory.forEach(msg => {
        const div = document.createElement("div");

        div.className =
            msg.role === "user"
                ? "user-msg"
                : "bot-msg";

        div.innerText = msg.text;

        chatBox.appendChild(div);
    });

    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const userMessage = input.value.trim();

    if (!userMessage) return;

    addUserMessage(userMessage);

    input.value = "";

    const botNode = addBotMessage("Thinking...");

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

        chatHistory.push({
            role: "bot",
            text: data.response
        });

        saveHistory();

    } catch (err) {
        botNode.innerText = "Server error.";
    }
}

input.addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

loadChatHistory();