document.addEventListener("DOMContentLoaded", () => {

    const term = new Terminal({
        fontFamily: 'Fira Mono, monospace',
        fontSize: 14,
        theme: { background: '#000000', foreground: '#FF7F11', cursor: '#FF8C42' }
    });

    const socket = io();

    const terminalDiv = document.getElementById('terminal');
    if (!terminalDiv) return console.error("Error: #terminal div not found");
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

    // --- Salida de texto normal ---
    socket.on("output", data => {
        term.write(data);
        term.prompt();
    });

    // --- Salida de gráficos ---
    socket.on("graph", data => {
        const graphicsDiv = document.getElementById("graphics");
        const img = document.createElement("img");

        img.src = "data:image/png;base64," + data;
        graphicsDiv.appendChild(img);

        const wrapper = document.getElementById("terminal-wrapper");
        wrapper.scrollTop = wrapper.scrollHeight;
    });

    // --- Fin del ejercicio ---
    socket.on("end", () => {
        finished = true;
        term.write("\r\n[✔] Exercise finished. Press Enter or Close button.\r\n");
        const closeBtn = document.getElementById("close-btn");
        if (closeBtn) closeBtn.style.display = "inline-block";
    });

    // --- Función cerrar popup ---
    function closePopup() {
        const overlay = document.getElementById("overlay");
        overlay.style.opacity = 0;
        setTimeout(() => {
            overlay.style.display = "none";
            window.location.href = "/";
        }, 300);
    }

    const closeBtn = document.getElementById("close-btn");
    if (closeBtn) closeBtn.addEventListener("click", closePopup);
});