import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from m8n.utils.filters import command


from m8n.config import BOT_USERNAME
from m8n.config import START_PIC
from m8n.config import BOT_NAME
from m8n.config import UPDATE
from m8n.config import OWNER_USERNAME



@Client.on_message(command("/start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f""" ياެهݪاެ {message.from_user.mention()} 🫶🏻\n
ياެعيۅني اެني بۅت بسيط مقدم من مطوࢪي يمديني اެشغݪ أغاެني في مجمۅعتك 🤍 .
""",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🥇 اެضفني اެݪى مجمۅعتَك 🥇", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton("طࢪيقة اެݪتشغيݪ", callback_data="user_guide")
                ],[
                    InlineKeyboardButton("اެݪاۅاެمࢪ", callback_data="command_list"),
                    InlineKeyboardButton("🦎 اެݪمطَۅࢪ", url=f"https://t.me/{OWNER_USERNAME}")                    
                ],
            ]
        ), 
    )


@Client.on_message(command(["السورس", f"مطور السورس"]) & filters.group & ~filters.edited)
async def gcstart(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9a0b3e3e819ef468a3063.jpg",
        caption=f" [‹ السورس ›](http://t.me/Tbiix)",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("‹ مطور السورس ›", url=f"https://t.me/nnnnnnnnnr")
                ]
            ]
        ),
    )


