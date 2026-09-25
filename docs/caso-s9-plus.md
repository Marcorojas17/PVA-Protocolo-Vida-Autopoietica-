# Caso: ECC y TMO crónicos en Samsung S9+ (SM-G9650)

**Dispositivo:** SM-G9650 (Galaxy S9+, Snapdragon, UFS)
**Sistema:** Android 10 · build G9650ZHU9FWC3
**Periodo analizado:** marzo 2025 → enero 2026 (10 meses)
**Método:** análisis de logs `m0_history` con PVA
**Herramienta:** https://marcorojas17.github.io/PVA-Protocolo-Vida-Autopoietica-/pva.html

---

## Qué se encontró

(Reemplaza estos valores con los números reales que arroja el análisis)

- **ECC acumulados:** XX
- **TMO acumulados:** YY
- **Pico TMO:** NN en YYYY-MM-DD
- **Periodo activo:** 10 meses continuos
- **Cantidad de entradas con anomalía:** ZZ

---

## Qué significa

**ECC** = Error Correction Code. Cada evento ECC representa una corrección de datos que realizó el controlador UFS. Uno o dos al mes es estadísticamente normal. XX en 10 meses es un patrón sostenido.

**TMO** = Timeout. El chip no respondió a tiempo a una operación de I/O. Aislado es ruido. Acumulativo es tendencia.

Los logs `m0_history` de Samsung registran estos contadores en el firmware, no en el sistema operativo. Persisten entre reinicios. Son un expediente silencioso del estado real del chip.

---

## Qué NO significa

No es falla terminal. El dispositivo opera con normalidad y no presenta síntomas visibles para el usuario.

Tampoco es una conspiracion: es telemetría de hardware que Samsung registra por diseño, sin dashboard público para interpretarla.

---

## Cómo verificarlo en tu propio dispositivo

1. Extrae los logs `m0_history_*.txt` de tu teléfono Samsung (ruta típica: `fsdbg`)
2. Abre https://marcorojas17.github.io/PVA-Protocolo-Vida-Autopoietica-/pva.html
3. Pestaña **PANORAMA**
4. Carga los archivos `.txt`
5. Presiona **ANALIZAR TODO**
6. Si el cuadro ámbar muestra ECC y TMO > 0, tienes el mismo patrón

La herramienta corre 100% en el navegador. No sube nada a ningún servidor. Nada sale de tu dispositivo.

---

## Cómo lo detecté

La herramienta PVA nació como parte del proyecto Protocolo Vida Autopoiética (MD-33). El motor de parseo se diseñó para leer los formatos `m0_history`, `u_history`, `us_history` y `ulc_history` que produce el subsistema de diagnóstico de Samsung.

Al aplicar el análisis sobre los logs de un S9+ en uso continuo desde 2023, los contadores ECC y TMO aparecieron desde marzo 2025 y se mantuvieron activos hasta el corte del análisis en enero 2026.

El patrón no es exclusivo de este equipo. Se puede reproducir en cualquier S9+ cuyos logs estén disponibles.

---

## Herramienta

**PVA · Consola Unificada**
https://marcorojas17.github.io/PVA-Protocolo-Vida-Autopoietica-/pva.html

- Parser en JavaScript puro
- Sin backend
- Sin telemetría
- SHA-256 calculado localmente
- Código fuente abierto: https://github.com/marcorojas17/PVA-Protocolo-Vida-Autopoietica-

---

*PVA · Protocolo Vida Autopoiética*
*Como es arriba, es en el commit.*