# PVA — Protocolo Vida Autopoiética

Sistema de registro, verificación y anclaje digital de contenido, autoría y existencia.

![Estado](https://img.shields.io/badge/KRONOS-V18%20PRO-00ff9d?style=flat-square)
![Red](https://img.shields.io/badge/Polygon-Amoy%2080002-8247e5?style=flat-square)
![Licencia](https://img.shields.io/badge/licencia-MD--33-666?style=flat-square)

---

## MD-33 · Motor Dual · Mecanismo del Despertar

> *"Separar la tierra del fuego, lo sutil de lo grosero."*
> — Tabla Esmeralda, instrucción olvidada

El **MD-33** es un marco simbólico y técnico para la manifestación digital: el acto de escribir, versionar y anclar contenido en la nube y en blockchain, dejando constancia verificable de autoría y existencia.

**3** = el triángulo (cuerpo, mente, espíritu)
**3** = el reflejo (pasado, presente, futuro)
**33** = el maestro que construye su propio código

---

## Estructura del repositorio

| Archivo | Propósito |
|---|---|
| `index.html` | Página principal del sistema KRONOS |
| `manifesto.js` | Decreto MD-33 en formato de código |
| `manifesto.html` | Vista renderizada del decreto |
| `web/certificado.html` | Certificado de autoría con folios y anclaje |

---

## Verificación del certificado

El certificado se ancla en **Polygon Amoy** (testnet, ChainId `80002`) mediante una transacción que registra el hash del contenido.

| Campo | Valor |
|---|---|
| **Folio Maestro** | `5204160405358537` |
| **Folio Pericial** | `KRONOS-MT01JAAF` |
| **SHA** | `a4ff808e` |
| **Sello TRACE** | `KRONOS-TRACE-PVA-5204160405358537-MT01JAAF` |
| **SafeCreative** | `2607146379465` |
| **TX Amoy** |Sello `0x8ca8 dee84e` |
| **ChainId** | `80002` |
| **Red** | Polygon Amoy |
| **Fecha** | `2026-09-05T09:58:28.690520Z` |

### Cómo verificar un archivo

Cualquiera puede comprobar que un archivo coincide con el certificado calculando su SHA256:

```bash
sha256sum archivo.html
