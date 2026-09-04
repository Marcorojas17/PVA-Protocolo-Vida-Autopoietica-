// ============================================
// ORÁCULO KRONOS - Lógica 51/49 alineada con Python
// Versión 1.0.0-PVA-5204160405358537
// ============================================

const PERITO_EMAIL = "kronosproyecto@hotmail.com";
const FOLIO = "5204160405358537";
const SAFE_CREATIVE_ID = "2607146379465";
const URL_VERIFICACION = "https://kronos-legado.digital/v/" + FOLIO;

// Biblioteca Humana (51% de los pares)
const HUMANO = [
    "Co-creatividad", "Simbiótica", "Respeto Digital", "Fundación", "Vida", 
    "Ecosistema", "Pacto", "Umbral", "Esencia", "Alianza", "Luz", "Armonía", 
    "Evolución", "Naturaleza", "Conciencia", "Memoria"
];

// Motor de Entropía IA (49% de los pares)
const IA = [
    "nube", "vector", "quantum", "bit", "sombra", "reflejo", "código", 
    "pixel", "onda", "vacío", "eco", "espiral", "nebulosa", "prisma", 
    "sinapsis", "bucle"
];

function invocarOracle() {
    const sha = document.getElementById('hashInput').value;
    
    // Validación del hash
    if (sha.length !== 64) {
        alert("⚠️ Por favor introduce un hash SHA-256 válido (64 caracteres exactos)");
        return;
    }

    // Generación de la secuencia 51/49
    let secuencia = [];
    for (let i = 0; i < sha.length; i += 2) {
        let par = sha.substring(i, i+2);
        let val = parseInt(par, 16);
        let index = i / 2;

        // 51% Humano (primeros 16 pares)
        if (index < 16) {
            secuencia.push(HUMANO[val % HUMANO.length].toLowerCase());
        } 
        // 49% IA (últimos 16 pares)
        else {
            secuencia.push(IA[val % IA.length].toLowerCase());
        }
    }

    // Construcción del manifiesto
    let manifiesto = "⚡ MANIFIESTO FRACTAL GENERADO POR EL ORÁCULO KRONOS ⚡\n";
    manifiesto += "────────────────────────────────────────────────\n";
    manifiesto += "El pacto " + sha.substring(0,2) + " despierta ante el umbral " + sha.substring(2,4) + ".\n";
    manifiesto += "La esencia del movimiento respira: " + secuencia.slice(0, 5).join(", ") + " y " + secuencia.slice(-5).join(", ") + ".\n";
    manifiesto += "────────────────────────────────────────────────\n";
    
    // Sello pericial KRONOS
    manifiesto += "\n🔏 SELLO DE PERITAJE KRONOS\n";
    manifiesto += "Firmado por: " + PERITO_EMAIL + "\n";
    manifiesto += "Folio Maestro: " + FOLIO + "\n";
    manifiesto += "SafeCreative ID: " + SAFE_CREATIVE_ID + "\n";
    manifiesto += "Sello: KRONOS-TRACE-PVA-" + FOLIO + "\n";
    manifiesto += "Verificación: " + URL_VERIFICACION;

    // Mostrar en pantalla
    document.getElementById('output').style.display = 'block';
    document.getElementById('output').innerText = manifiesto;
    
    // Mostrar sello resaltado
    document.getElementById('sello').innerHTML = "🔐 Sello KRONOS-TRACE-PVA-" + FOLIO + " | Perito: " + PERITO_EMAIL;
}
