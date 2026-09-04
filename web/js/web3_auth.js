/**
 * PVA - Módulo de autenticación Web3 y pago.
 * Conecta con MetaMask, firma mensajes y verifica transacciones.
 */
const FOLIO = "5204160405358537";
const PERITO = "kronosproyecto@hotmail.com";
const GENESIS_SHA256 = "41a3683bbf83296eeb45da9b0e0ea5a7c095e78b493772e79520a92dbc39f4c3";

let web3;
let userAccount;
// ⚠️ Reemplaza con la dirección de tu contrato deployado en Sepolia/Mainnet
const contractAddress = "0xPON_AQUI_TU_CONTRATO_DEPLOYADO";
const abi = []; // ABI del contrato (completa aquí)

async function connectWallet() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            userAccount = accounts[0];
            web3 = new Web3(window.ethereum);
            console.log("Wallet conectada:", userAccount, "| Folio:", FOLIO);
            updateUI();
            return true;
        } catch (error) {
            console.error("Usuario rechazó la conexión", error);
            return false;
        }
    } else {
        alert("Por favor instala MetaMask");
        return false;
    }
}

async function payForDictamen(priceInWei) {
    if (!web3 || !userAccount) {
        await connectWallet();
    }
    try {
        const tx = {
            from: userAccount,
            to: contractAddress,
            value: priceInWei,
            gas: 21000
        };
        const txHash = await web3.eth.sendTransaction(tx);
        console.log("Transacción enviada:", txHash, "| Perito:", PERITO);
        await generateManifestoWithPayment(txHash);
        return txHash;
    } catch (error) {
        console.error("Error en el pago", error);
        return null;
    }
}

async function generateManifestoWithPayment(txHash) {
    const response = await fetch('/api/generate-manifesto', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ txHash, userAccount, folio: FOLIO })
    });
    const data = await response.json();
    if (data.success) {
        window.location.href = data.url;
    } else {
        alert("Error al generar el dictamen");
    }
}

function updateUI() {
    const accountSpan = document.getElementById('account');
    if (accountSpan) accountSpan.textContent = userAccount;
    const connectBtn = document.getElementById('connectBtn');
    if (connectBtn) {
        connectBtn.textContent = "Wallet Conectada";
        connectBtn.disabled = true;
    }
}

window.addEventListener('load', () => {
    const connectBtn = document.getElementById('connectBtn');
    if (connectBtn) {
        connectBtn.addEventListener('click', connectWallet);
    }
});
