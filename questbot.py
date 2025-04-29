import logging
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Вставь сюда свой токен
TOKEN = "8003023840:AAE8D9V0oTkU2lrB0f0Lt_6S1FijwNIOnKQ"

# Включаем логирование для отладки
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Начальная сцена квеста
START_SCENE = (
    "You open your eyes. The room is round, the walls are gray like concrete.\n"
    "On the floor, you see three symbols made of metal strips:\n"
    "- Circle\n- Triangle\n- Square\n"
    "There's a narrow door without a handle ahead, and a blue light blinking above it.\n"
    "\nDescribe what you want to examine or where you want to move."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка команды /start."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!\nWelcome to the AI Quest.\n",
    )
    await update.message.reply_text(START_SCENE)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка обычных текстовых сообщений."""
    text = update.message.text.lower()

    if "circle" in text:
        await update.message.reply_text("The circle feels cold to the touch.")
    elif "triangle" in text:
        await update.message.reply_text("The triangle has small scratches on its edges.")
    elif "square" in text:
        await update.message.reply_text("The square looks brand new, untouched.")
    elif "door" in text:
        await update.message.reply_text("The door doesn't budge. Maybe a symbol needs to be activated?")
    else:
        await update.message.reply_text("I can't recognize that. Try describing one of the symbols or the door.")

def main() -> None:
    """Запуск бота."""
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
