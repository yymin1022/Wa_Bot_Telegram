from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update

import base64
import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN", "NO_TOKEN")
WA_API_SERVER = os.getenv("WA_API_SERVER", "localhost:8080")


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="와.. 역시;;")


async def sendMessage(update, context):
    message_text = update.message.text or update.message.caption or ""
    await sendWaMessage(message_text, update, context)


async def sendWaMessage(message, update, context):
    if update.effective_user.is_bot == False:
        image_base64 = None
        if update.message.photo:
            photo = update.message.photo[-1]
            photo_file = await context.bot.get_file(photo.file_id)
            img_bytearray = await photo_file.download_as_bytearray()
            image_base64 = base64.b64encode(img_bytearray).decode("utf-8")

        requestData = dict([("msg", message), ("room", str(update.effective_chat.id)), ("sender", str(update.effective_user.id))])
        if image_base64:
            requestData["image"] = image_base64

        resultData = requests.post(f"{WA_API_SERVER}/getMessage", json=requestData).json()

        resultMessage = resultData["DATA"]["msg"]

        if resultData["RESULT"]["RESULT_CODE"] == 0:
            if resultMessage.find("\\m") > 0:
                resultMessageList = resultMessage.split("\\m")

                for resultMessageItem in resultMessageList:
                    await context.bot.send_message(chat_id=update.effective_chat.id, text=resultMessageItem)
            else:
                resultMessage = resultMessage.replace("\\n", "\n")
                await context.bot.send_message(chat_id=update.effective_chat.id, text=resultMessage)


def main():
    application = Application.builder().token(TOKEN).build()

    messageHandler = MessageHandler(filters.TEXT | filters.PHOTO, sendMessage)
    application.add_handler(messageHandler)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()