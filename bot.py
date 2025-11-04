import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")

ITEMS = [
    "RX 9060 XT 8GB",
    "RX 9060 XT 16GB",
    "RTX 3060",
    "RTX 4060",
    "GTX 1660 SUPER",
]

async def start(update, context):
    await update.message.reply_text("✅ Bot ativo! Envie o nome de um item para pesquisar.")

async def search(update, context):
    query = update.message.text.lower()
    results = [item for item in ITEMS if query in item.lower()]

    if results:
        response = "🔍 Resultados encontrados:\n" + "\n".join(f"- {item}" for item in results)
    else:
        response = "❌ Nenhum item encontrado."

    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    app.run_polling()

if __name__ == "__main__":
    main()
