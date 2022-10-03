from config import EVENT_LOGS
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(EVENT_LOGS, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + EVENT_LOGS
            else:
                chat_info = await bot.get_chat(EVENT_LOGS)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://telegra.ph/file/ba582d379f2586f227d66.png", caption=f"Gabung Group dibawah dulu lalu coba /start lagi!",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🥺 Gabung Group Sini 🥺", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {EVENT_LOGS} !")
