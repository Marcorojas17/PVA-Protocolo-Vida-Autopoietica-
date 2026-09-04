// ═══════════════════════════════════════════
// ORÁCULO BIO-CRIPTOGRÁFICO KRONOS
// ═══════════════════════════════════════════

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let particles = [];
let connections = [];
let organismVisible = false;
let animationId;
let seed = 0;

// Identidad KRONOS
const PERITO = "kronosproyecto@hotmail.com";
const FOLIO = "5204160405358537";
const SAFE_ID = "2607146379465";

// Palabras 51% humano / 49% IA
const HUMAN = ["co-creatividad","simbiótica","respeto digital","fundación","vida","ecosistema","pacto","umbral","esencia","alianza","luz","armonía"];
const IA = ["nube","vector","quantum","bit","sombra","reflejo","código","pixel","onda","vacío","eco","espiral"];

// ── Configuración de tamaño ──
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

// ── Generar red fractal a partir del hash ──
function generateOrganism(hash) {
    particles = [];
    connections = [];

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const scale = Math.min(canvas.width, canvas.height) / 2.5;

    // Creamos un nodo central (el "gen")
    particles.push({ x: centerX, y: centerY, vx: 0, vy: 0, r: 6, type: 'core' });

    // Generamos ramas usando pares del hash
    for (let i = 0; i < 64; i += 2) {
        const byte = parseInt(hash.substring(i, i+2), 16);
        const angle = (byte / 255) * Math.PI * 2 + (i * 0.1);
        const distance = (byte / 255) * scale * 0.8 + scale * 0.2;
        const x = centerX + Math.cos(angle) * distance;
        const y = centerY + Math.sin(angle) * distance;

        const newParticle = { x, y, vx: 0, vy: 0, r: 3 + (byte % 5), type: 'branch' };
        particles.push(newParticle);

        // Conexión al nodo anterior en la secuencia
        if (i >= 2) {
            connections.push({ a: particles.length - 2, b: particles.length - 1 });
        } else {
            connections.push({ a: 0, b: 1 });
        }
    }

    // Colores derivados del hash
    const r = parseInt(hash.substring(0, 2), 16);
    const g = parseInt(hash.substring(2, 4), 16);
    const b = parseInt(hash.substring(4, 6), 16);
    seed = (r + g + b) % 360;

    organismVisible = true;
    startAnimation();
}

// ── Animación ──
function startAnimation() {
    if (animationId) cancelAnimationFrame(animationId);
    let time = 0;

    function draw() {
        time += 0.02;
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Fondo oscuro con gradiente
        const gradient = ctx.createRadialGradient(canvas.width/2, canvas.height/2, 50, canvas.width/2, canvas.height/2, canvas.width/2);
        gradient.addColorStop(0, `hsla(${seed}, 80%, 10%, 1)`);
        gradient.addColorStop(1, '#000');
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Dibujar conexiones (red fractal)
        ctx.lineWidth = 1.2;
        for (const conn of connections) {
            const a = particles[conn.a];
            const b = particles[conn.b];
            if (!a || !b) continue;
            const alpha = 0.4 + Math.sin(time * 3) * 0.2;
            ctx.strokeStyle = `hsla(${seed}, 90%, 60%, ${alpha})`;
            ctx.beginPath();
            ctx.moveTo(a.x, a.y);
            ctx.lineTo(b.x, b.y);
            ctx.stroke();
        }

        // Dibujar partículas
        for (const p of particles) {
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
            ctx.fillStyle = p.type === 'core' ? '#d4af37' : `hsla(${seed}, 100%, 70%, 0.9)`;
            ctx.shadowBlur = p.type === 'core' ? 30 : 10;
            ctx.shadowColor = p.type === 'core' ? '#d4af37' : `hsla(${seed}, 100%, 70%, 1)`;
            ctx.fill();
        }

        // Efecto de respiración
        ctx.globalAlpha = 0.3;
        ctx.beginPath();
        ctx.arc(canvas.width/2, canvas.height/2, 80 + Math.sin(time * 2) * 10, 0, Math.PI * 2);
        ctx.strokeStyle = '#00ffcc';
        ctx.stroke();
        ctx.globalAlpha = 1;

        animationId = requestAnimationFrame(draw);
    }
    draw();
}

// ── Generar manifiesto con sello ──
function invocarOracle() {
    const hashInput = document.getElementById('hashInput').value.trim().toLowerCase();
    if (hashInput.length !== 64 || /[^a-f0-9]/.test(hashInput)) {
        alert('⚠️ Introduce un hash SHA-256 válido (64 caracteres hexadecimales)');
        return;
    }

    // Generar organismo visual
    generateOrganism(hashInput);

    // Crear secuencia 51% humano / 49% IA
    const sequence = [];
    for (let i = 0; i < hashInput.length; i += 2) {
        const val = parseInt(hashInput.substring(i, i+2), 16);
        if (i < 32) { // 51% primeros 16 pares
            sequence.push(HUMAN[val % HUMAN.length]);
        } else { // 49% restantes
            sequence.push(IA[val % IA.length]);
        }
    }

    // Construir manifiesto
    const manifiesto = `⚡ MANIFIESTO FRACTAL GENERADO\n─────────────────────────────\nEl génesis ${hashInput.substring(0, 8)}... ha despertado.\nLa criatura fractal respira: ${sequence.slice(0, 6).join(", ")}...\n─────────────────────────────\n\n🔏 SELLO PERICIAL KRONOS\nFOLIO:${FOLIO}\nPERITO:${PERITO}\nGENESIS:${hashInput}\nSello: KRONOS-TRACE-PVA-${FOLIO}`;

    // Mostrar manifiesto
    const output = document.getElementById('oracle-output');
    output.style.display = 'block';
    output.innerText = manifiesto;

    // Mostrar sello brillante
    const seal = document.getElementById('seal');
    seal.style.display = 'block';
    seal.innerText = `🔐 KRONOS TRACE · Folio ${FOLIO} · Verificado por ${PERITO}`;
}
