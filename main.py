from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update

import asyncio
import base64
import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN", "NO_TOKEN")
WA_API_SERVER = os.getenv("WA_API_SERVER", "localhost:8080")
if not WA_API_SERVER.startswith("http://") and not WA_API_SERVER.startswith("https://"):
    WA_API_SERVER = f"http://{WA_API_SERVER}"


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

        reply_prefix = ""
        if update.message.reply_to_message:
            orig = update.message.reply_to_message
            if not image_base64 and orig.photo:
                try:
                    photo = orig.photo[-1]
                    photo_file = await context.bot.get_file(photo.file_id)
                    img_bytearray = await photo_file.download_as_bytearray()
                    image_base64 = base64.b64encode(img_bytearray).decode("utf-8")
                except Exception as e:
                    print(f"[Error] Failed to download reply original photo: {e}")
            
            orig_user = orig.from_user.first_name if orig.from_user else "알 수 없음"
            orig_text = orig.text or orig.caption or ""
            if not orig_text and orig.photo:
                orig_text = "📎 [사진 첨부됨]"
            elif not orig_text and orig.document:
                orig_text = "📎 [첨부파일]"
                
            reply_prefix = f"(답장 대상: {orig_user}님의 메시지 \"{orig_text}\")\n---\n"

        message_content_to_send = reply_prefix + message
        requestData = dict([("msg", message_content_to_send), ("room", str(update.effective_chat.id)), ("sender", str(update.effective_user.id))])
        if image_base64:
            requestData["image"] = image_base64

        url = WA_API_SERVER
        if not url.endswith("/getMessage"):
            if url.endswith("/"):
                url = f"{url}getMessage"
            else:
                url = f"{url}/getMessage"

        try:
            response = await asyncio.to_thread(
                requests.post,
                url,
                json=requestData,
                timeout=10
            )
            resultData = response.json()
        except Exception as e:
            print(f"[Error] Failed to connect or parse response: {e}")
            return

        if (not isinstance(resultData, dict) or 
            "RESULT" not in resultData or 
            "DATA" not in resultData or 
            "msg" not in resultData["DATA"]):
            print(f"[Error] Invalid response structure: {resultData}")
            return

        resultMessage = resultData["DATA"]["msg"]

        if resultData["RESULT"]["RESULT_CODE"] == 0:
            if resultMessage.find("\\m") > 0:
                resultMessageList = resultMessage.split("\\m")

                for resultMessageItem in resultMessageList:
                    await context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        reply_to_message_id=update.message.message_id,
                        text=resultMessageItem)
            else:
                resultMessage = resultMessage.replace("\\n", "\n")
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    reply_to_message_id=update.message.message_id,
                    text=resultMessage)


def main():
    application = Application.builder().token(TOKEN).build()

    messageHandler = MessageHandler(filters.TEXT | filters.PHOTO, sendMessage)
    application.add_handler(messageHandler)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()