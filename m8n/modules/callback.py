from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from m8n.config import BOT_USERNAME
from m8n.config import START_PIC
from m8n.config import OWNER_ID
from m8n.config import ASSUSERNAME
from m8n.config import UPDATE
from m8n.config import SUPPORT
from m8n.config import OWNER_USERNAME
from m8n.config import BOT_NAME


@Client.on_callback_query(filters.regex("cbhome"))
async def cbhome(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" {message.from_user.mention()} 🫶🏻\n
صِبَاެحِكَ سِكَࢪ ۅٛحِݪيَبَ ، مِمِكَنِ تَضِيَفَنِيَ حِتَىِ اެجَيَبَ ؟ 🐥.
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اެݪاެعداެداެت", callback_data="cbabout"),
                ],
                [

                    InlineKeyboardButton(
                        "اެݪاެوِاެمࢪ", callback_data="cbevery")
                ],
                [
                    InlineKeyboardButton(
                        "🥇 اެضفني اެݪى مجموعتَك 🥇", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds_set(_, query: CallbackQuery):
        await query.answer("commands menu")
        await query.edit_message_text(
        f"""‹ اوامر البوت › [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 

- يمديك تشوف كل الاوامر عن طريق الازرار أدناه -""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اެوَاެمࢪ اެݪمطوِࢪين .", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Everyone", callback_data="cbevery"),
                    InlineKeyboardButton("اެوَاެمࢪ اެݪمشࢪفين .", callback_data="cbadmins"),
                ],[
                    InlineKeyboardButton("ࢪجَۅَعَ", callback_data="cbhome")
                ],
            ]
        ),
    ) 


# Commands for Everyone !!
@Client.on_callback_query(filters.regex("cbevery"))
async def all_set(_, query: CallbackQuery):
    await query.answer("Everyone menu")
    await query.edit_message_text(
    f""" ‹ مرحبا بك في قسم الاوامر ›

- شغل | بالرد على ملف او اسم اغنية للتشغيل  .

- يوت | باسم الاغنية لتحميل اغنية من اليوتيوب .

- رابط | لحصول على رابط اغنية من يوت .

- بنك | لفحص بنك البوت والسرعة الممكنه .

- تج | لتحويل صورة الى رابط تليجراف .

- شكراً لقرائتك الاوامر  أتمنى لك يوماً تعيساً  . 🤎""",
        reply_markup=InlineKeyboardMarkup(
            [
              [
                    InlineKeyboardButton(
                        "اެۅٛاެمࢪ اެݪمشࢪفين .", callback_data="cbadmins"),
                    InlineKeyboardButton(
                        "اެواެمࢪ اެݪمطوِࢪين .", callback_data="cbsudo")
                ],
              [InlineKeyboardButton("ࢪجَۅَعَ", callback_data="cbhome")]]
        ),
    )


# Commands for SudoUsers
@Client.on_callback_query(filters.regex("cbsudo"))
async def sudo_set(_, query: CallbackQuery):
    await query.answer("sudo menu")
    await query.edit_message_text(
    f""" ‹ مرحبا بك في قسم اوامر المطورين ›

- الاحصائيات | لرؤية احصائيات البوت اخر شهر .

- ريستارت | اعادة تشغيل البوت وتحسين السرعة .

- اذاعة | لعمل اذاعة في المجموعات بدون تثبيت .

- رسالة | لعمل اذاعة لكل المجموعات مع التثبيت .

- المغادرة | لمغادرة حساب المساعد من المجموعات .

- شكراً لقرائتك الاوامر  أتمنى لك يوماً تعيساً  . 🤎""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ࢪجَۅَعَ", callback_data="cbevery")
                ],
            ]
        ),
    )


# Commands for Group Admins
@Client.on_callback_query(filters.regex("cbadmins"))
async def admin_set(_, query: CallbackQuery):
    await query.answer("admins menu")
    await query.edit_message_text(
    f""" ‹ مرحبا بك في قسم اوامر المشرفين ›

- كافي | ايقاف تشغيل الاغنية في المجموعة .

- سكب | تخطي التالية الأغنية في المجموعة .

- مؤقتا | لإيقاف تشغيل الأغنية مؤقتا .

- استمر | استمرار التشغيل المتوقف مؤقتا .

- تنظيف | لتنظيف التشغيل وتحسين سرعة البوت .

- انضم | للانضمام حساب المساعد الى المجموعة .

- غادر | لمغادرة حساب المساعد المجموعة .

- شكراً لقرائتك الاوامر  أتمنى لك يوماً تعيساً  . 🤎""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ࢪجَۅَعَ", callback_data="cbevery")
                ],
            ]
        ),
    )


# Bot about & Information
@Client.on_callback_query(filters.regex("cbabout"))
async def about_set(_, query: CallbackQuery):
    await query.edit_message_text(
    f"""‹ أمر قسم الاعدادات  › [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

- يمديك الانضمام والتواصل مع المطورين عن طريق الازرار التحت """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("قناެة اެݪدعم .", url=f"https://t.me/{SUPPORT}"),
                    InlineKeyboardButton("قناެة اެݪمطوَࢪ", url=f"https://t.me/{UPDATE}")
                ],[
                    InlineKeyboardButton("🦎 اެݪمطوࢪ", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("حساެب اެݪمساެعد .", url=f"https://t.me/{ASSUSERNAME}")
                ],[
                    InlineKeyboardButton("‹ السورس ›", url="https://t.me/Xl444")
                ],[
                    InlineKeyboardButton("ࢪجَۅعَ", callback_data="cbhome")
                ],
            ]
        ),
    )


