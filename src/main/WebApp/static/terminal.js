document.addEventListener("DOMContentLoaded", () => {

    const term = new Terminal({
        fontFamily: 'Fira Mono, monospace',
        fontSize: 14,
        theme: {
            background: '#000000',
            foreground: '#00ffff',
            cursor: '#00ffff'
        }
    });

    const socket = io();

    const terminalDiv = document.getElementById('terminal');
    if (!terminalDiv) {
        console.error("Error: #terminal div not found");
        return;
    }
    term.open(terminalDiv);

    const fileName = window.exerciseData?.fileName || "example.txt";
    const exerciseId = window.exerciseData?.exerciseId || 0;

    term.write(`Loading the practice exercise: ${fileName}.\r\n`);

    let inputBuffer = "";
    let finished = false;

    socket.emit("start_exercise", { file_name: fileName, exercise_id: exerciseId });

    term.prompt = () => { term.write("\r\n"); };

    term.onData(e => {
        if (finished) {
            if (e === '\r') closePopup();
            return;
        }

        if (e === '\r') {
            socket.emit("input", inputBuffer);
            term.write("\r\n");
            inputBuffer = "";
        } else if (e === '\u007F') {
            if (inputBuffer.length > 0) {
                inputBuffer = inputBuffer.slice(0, -1);
                term.write('\b \b');
            }
        } else {
            inputBuffer += e;
            term.write(e);
        }
    });

    socket.on("output", data => {
        term.write(data);
        term.prompt();
    });

    socket.on("end", () => {
        finished = true;
        term.write("\r\n[✔] Exercise finished. Press Enter to return to the menu.\r\n");
        const closeBtn = document.getElementById("close-btn");
        if (closeBtn) closeBtn.style.display = "inline-block";
    });

    function closePopup() {
        window.location.href = "/";
    }

    const closeBtn = document.getElementById("close-btn");
    if (closeBtn) closeBtn.addEventListener("click", closePopup);

});