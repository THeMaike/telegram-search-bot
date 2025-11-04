import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

ITEMS = [
    {"nome": "RX 9060 XT 8GB", "tags": ["rx 9060 xt", "8gb", "9060 8"]},
    {"nome": "RX 9060 XT 16GB", "tags": ["rx 9060 xt", "16gb", "9060 16"]},
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot online! Envie o nome de um item para pesquisar.")

async def search_item(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    results = []

    for item in ITEMS:
        if any(tag in query for tag in item["tags"]):
            results.append(item["nome"])

    if results:
        await update.message.reply_text("✨ Resultados encontrados:\n" + "\n".join(results))
    else:
        await update.message.reply_text("❌ Nenhum item encontrado.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_item))

    app.run_polling()

if __name__ == "__main__":
    main()
