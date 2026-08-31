<div align="center">

# 🌍 Country Info Bot

**A Telegram bot that answers questions about countries — capital, region and structure**

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="python" />
  <img src="https://img.shields.io/badge/Telegram_Bot-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="telegram" />
</p>

<p>
  <a href="https://github.com/Raximboy7/country_structure_bot/stargazers"><img src="https://img.shields.io/github/stars/Raximboy7/country_structure_bot?style=flat-square&color=8B5CF6&labelColor=0D1117" alt="stars" /></a>
  <a href="https://github.com/Raximboy7/country_structure_bot/commits"><img src="https://img.shields.io/github/last-commit/Raximboy7/country_structure_bot?style=flat-square&color=8B5CF6&labelColor=0D1117" alt="last commit" /></a>
  <a href="https://github.com/Raximboy7/country_structure_bot/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-8B5CF6?style=flat-square&labelColor=0D1117" alt="license" /></a>
</p>

</div>

---


## 📖 Overview

A menu-driven Telegram bot built with `pyTelegramBotAPI`. Handlers are split into a package, the bot registers its own command list on startup, and keyboards guide the user through the available information.


## ✨ Features

- 🌍 **Country lookup** through a guided menu
- ⌨️ **Custom keyboards** defined in one module
- 📋 **Auto-registered command list** (`/start`, `/help`) via `set_my_commands`
- 🗂 **Package layout** — `handlers/`, `keyboards.py`, `loader.py`, `config.py`
- 🔐 **Token from environment**



## 🚀 Getting Started

```bash
# 1 — clone
git clone https://github.com/Raximboy7/country_structure_bot.git
cd country_structure_bot

# 2 — virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3 — dependencies
pip install -r requirements.txt

# 4 — environment variables
cp .env.example .env              # add your token

# run
python bot.py
```


## 🔧 Configuration

Copy `.env.example` to `.env` and fill in your own values. **`.env` is git-ignored — never commit it.**

| Variable | Description | Default |
|---|---|---|
| `BOT_TOKEN` | Telegram bot token from @BotFather | — |


## 📁 Project Structure

```
country_structure_bot/
├── bot.py             # entry point
├── loader.py          # bot instance + command registration
├── config.py          # reads BOT_TOKEN from .env
├── keyboards.py
└── handlers/
    ├── commands.py
    └── bot_handlers.py
```


## 🗓 Roadmap

- [ ] Pull live data from the REST Countries API
- [ ] Country flags and maps
- [ ] Inline search mode
- [ ] Multi-language answers


---

<details>
<summary><b>🇺🇿 &nbsp;O'zbekcha tavsif</b></summary>

<br/>

## 📖 Loyiha haqida

`pyTelegramBotAPI` asosidagi menyuli Telegram bot. Handler'lar alohida paketga ajratilgan, bot ishga tushganda o'z buyruqlar ro'yxatini ro'yxatdan o'tkazadi.

## 🚀 Ishga tushirish

```bash
# 1 — clone
git clone https://github.com/Raximboy7/country_structure_bot.git
cd country_structure_bot

# 2 — virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3 — dependencies
pip install -r requirements.txt

# 4 — environment variables
cp .env.example .env              # add your token

# run
python bot.py
```

</details>

---

## 🤝 Contributing

Issue va Pull Request'lar ochiq. Katta o'zgarishdan oldin issue orqali muhokama qiling.

## 📄 License

MIT — batafsil [`LICENSE`](LICENSE) faylida.

## 👤 Author

<table>
<tr>
<td align="center">
<a href="https://github.com/Raximboy7"><img src="https://github.com/Raximboy7.png" width="80" alt="Raximboy Ibrohimov" /></a>
</td>
<td>

**Raximboy Ibrohimov**<br/>
Backend &amp; Mobile Developer · Tashkent, Uzbekistan 🇺🇿

[![Portfolio](https://img.shields.io/badge/Portfolio-8B5CF6?style=flat-square&logo=googlechrome&logoColor=white)](https://ibrohimov-dev.uz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raximboy-ibroximov-a75855268/)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/Raximboy7)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:raximboy4200@gmail.com)

</td>
</tr>
</table>

<div align="center">
<sub>⭐ Foydali bo'lsa, yulduzcha qoldiring!</sub>
</div>
