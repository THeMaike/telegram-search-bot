import difflib
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

# LISTA DE ITENS
itens = [
    "Monitor LG 27 polegadas",
    "Monitor Samsung 27 144hz",
    "Monitor AOC 27 144hz",
    "Teclado Mecânico Redragon Kumara",
    "Teclado Mecânico HyperX Alloy",
    "Mouse Gamer Logitech G203",
    "Mouse Razer Viper Mini",
    "Placa de Vídeo RTX 4060",
    "Placa de Vídeo RTX 4070",
    "Placa de Vídeo RX 9060 XT 8GB",
    "Placa de Vídeo RX 9060 XT 16GB",
    "Fonte Corsair 650w",
    "Fonte EVGA 500w",
    "SSD Kingston 480GB",
    "SSD NVMe 1TB Samsung",
]

def start(update, context):
    update.message.reply_text("Olá! Envie o nome do item que deseja pesquisar 🔎")

def pesquisar(query):
    query_lower = query.lower()

    # 1️⃣ Busca EXATA
    exatos = [item for item in itens if item.lower() == query_lower]
    if exatos:
        return "✅ Resultado exato encontrado:\n" + "\n".join(f"- {item}" for item in exatos)

    # 2️⃣ Busca PARCIAL
    parciais = [item for item in itens if query_lower in item.lower()]
    if parciais:
        return "🔎 Resultados encontrados (parcial):\n" + "\n".join(f"- {item}" for item in parciais)

    # 3️⃣ Busca SIMILAR
    parecidos = difflib.get_close_matches(query, itens, n=5, cutoff=0.2)
    if parecidos:
        return "🤏 Talvez você quis dizer:\n" + "\n".join(f"- {item}" for item in parecidos)

    return "❌ Nenhum item parecido foi encontrado."

def mensagem(update, context):
    texto = update.message.text
    resposta = pesquisar(texto)
    update.message.reply_text(resposta)

def main():
    TOKEN = os.getenv("TOKEN")  # Pega o token do ambiente

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, mensagem))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
