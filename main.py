import asyncio
import base64
import io
import os

from PIL import Image, ImageOps
import requests
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TELEGRAM_TOKEN", "NO_TOKEN")
WA_API_SERVER = os.getenv("WA_API_SERVER", "localhost:8080")
if not WA_API_SERVER.startswith("http://") and not WA_API_SERVER.startswith("https://"):
    WA_API_SERVER = f"http://{WA_API_SERVER}"


def process_image_to_base64(image_bytes: bytes) -> str:
    with Image.open(io.BytesIO(image_bytes)) as img:
        try:
            img = ImageOps.exif_transpose(img)
        except Exception:
            pass

        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")

        if max(img.width, img.height) > 1280:
            img.thumbnail((1280, 1280), Image.Resampling.LANCZOS)

        output_buffer = io.BytesIO()
        img.save(output_buffer, format="PNG", optimize=True)
        return base64.b64encode(output_buffer.getvalue()).decode("utf-8")


async def delayed_typing(chat, delay: float = 1.0):
    try:
        await asyncio.sleep(delay)
        await chat.send_action(action=ChatAction.TYPING)
    except asyncio.CancelledError:
        pass


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="와.. 역시;;")


async def sendMessage(update, context):
    message_text = update.message.text or update.message.caption or ""
    await sendWaMessage(message_text, update, context)


async def sendWaMessage(message, update, context):
    if update.effective_user.is_bot == False:
        images = []
        if update.message.photo:
            try:
                photo = update.message.photo[-1]
                photo_file = await context.bot.get_file(photo.file_id)
                img_bytearray = await photo_file.download_as_bytearray()
                images.append(process_image_to_base64(img_bytearray))
            except Exception as e:
                print(f"[Error] Failed to process message photo: {e}")

        reply_message = None
        if update.message.reply_to_message:
            orig = update.message.reply_to_message
            reply_images = []
            if orig.photo:
                try:
                    photo = orig.photo[-1]
                    photo_file = await context.bot.get_file(photo.file_id)
                    img_bytearray = await photo_file.download_as_bytearray()
                    reply_images.append(process_image_to_base64(img_bytearray))
                except Exception as e:
                    print(f"[Error] Failed to process reply original photo: {e}")
            
            orig_user = orig.from_user.first_name if orig.from_user else "알 수 없음"
            orig_text = orig.text or orig.caption or ""
            if not orig_text and orig.photo:
                orig_text = "📎 [사진 첨부됨]"
            elif not orig_text and orig.document:
                orig_text = "📎 [첨부파일]"
                
            reply_message = {
                "msg": orig_text,
                "sender": orig_user,
                "images": reply_images
            }

        requestData = {
            "msg": message,
            "room": str(update.effective_chat.id),
            "sender": str(update.effective_user.id),
            "images": images
        }
        if reply_message:
            requestData["replyMessage"] = reply_message

        url = WA_API_SERVER
        if not url.endswith("/getMessage"):
            if url.endswith("/"):
                url = f"{url}getMessage"
            else:
                url = f"{url}/getMessage"

        typing_task = asyncio.create_task(delayed_typing(update.message.chat, delay=1.0))
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
        finally:
            typing_task.cancel()

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
                    await update.message.reply_text(resultMessageItem)
            else:
                resultMessage = resultMessage.replace("\\n", "\n")
                await update.message.reply_text(resultMessage)


def main():
    application = Application.builder().token(TOKEN).build()

    messageHandler = MessageHandler(filters.TEXT | filters.PHOTO, sendMessage)
    application.add_handler(messageHandler)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()