# rss-puglia

Questo progetto genera un feed RSS aggiornato automaticamente con le ultime **notizie**, **eventi** e **bandi** pubblicati dalla [Regione Puglia](https://www.regione.puglia.it).

📦 Il feed può essere usato con:
- Microsoft Teams (via Power Automate)
- Lettori RSS (Feedly, Outlook, ecc.)
- Bot Telegram, WhatsApp, ecc.

---

## 🚀 Come funziona

🔧 Uno script Python (`genera_feed.py`) fa scraping da queste 3 pagine:

- 📰 Notizie: [elenco-notizie](https://www.regione.puglia.it/web/ricerca-e-relazioni-internazionali/elenco-notizie)
- 🎉 Eventi: [agenda-eventi](https://www.regione.puglia.it/web/ricerca-e-relazioni-internazionali/agenda-eventi)
- 📢 Bandi: [elenco-bandi](https://www.regione.puglia.it/web/ricerca-e-relazioni-internazionali/elenco-bandi)

📤 Ogni ora, una GitHub Action aggiorna il file `feed.xml` e lo pubblica su **GitHub Pages**.

---

## 📡 Link al feed RSS

Una volta attivato GitHub Pages:

