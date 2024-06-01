from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Import openAI
pip install openai

# Función que maneja el comando /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hola! Soy tu bot de Telegram.')

# Función que maneja los mensajes de texto
async def echo(update: Update, context: CallbackContext) -> None:
    print("Llego un mensaje")
    await update.message.reply_text(update.message.text)

def main() -> None:
    # Token del bot
    token = '7255111687:AAGckK5yhkZS7B0zbjnu2_Ghs9rvDAdJ2lM'
    
    # Crea la aplicación
    application = Application.builder().token(token).build()

    # Registra los manejadores de comandos
    application.add_handler(CommandHandler("start", start))

    # Registra el manejador para mensajes de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Inicia el bot
    application.run_polling()

if __name__ == '__main__':
    main()
