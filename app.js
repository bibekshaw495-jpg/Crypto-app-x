const priceEl = document.getElementById("price");
const messageEl = document.getElementById("message");

let balance = 10000; // demo balance
let btcHold = 0;

async function loadPrice() {
  try {
    const res = await fetch(
      "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    );
    const data = await res.json();
    priceEl.innerText = "$ " + data.bitcoin.usd;
  } catch (e) {
    priceEl.innerText = "Price Error";
  }
}

function buyBTC() {
  if (balance >= 1000) {
    balance -= 1000;
    btcHold += 0.001;
    messageEl.innerText = "✅ BTC Bought (Demo)";
  } else {
    messageEl.innerText = "❌ Not enough balance";
  }
}

function sellBTC() {
  if (btcHold > 0) {
    btcHold -= 0.001;
    balance += 1000;
    messageEl.innerText = "✅ BTC Sold (Demo)";
  } else {
    messageEl.innerText = "❌ No BTC to sell";
  }
}

loadPrice();
setInterval(loadPrice, 10000);
