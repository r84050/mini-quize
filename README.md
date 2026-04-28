# 🎯 Mini Quize

Telegram Mini App Quiz with AdSgram monetization.

## Deploy Steps

1. GitHub → New Repo → `mini-quize` → Public
2. Upload: index.html, bot.py, README.md
3. Settings → Pages → Branch: main → Save
4. Live: https://r84050.github.io/mini-quize/

## AdSgram Setup
- adsgram.ai → Create Block → Copy Block ID
- index.html line: `const ADSGRAM_BLOCK_ID = "YOUR_ID";`

## Bot Setup
- @BotFather → /newbot → copy token
- bot.py line: `BOT_TOKEN = "your_token"`
- pip install python-telegram-bot
- python bot.py
