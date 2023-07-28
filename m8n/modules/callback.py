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
        f""" ياެهݪاެ {message.from_user.mention()} 🫶🏻\n
ياެعيۅني اެني بۅت بسيط مقدم من مطوࢪي يمديني اެشغݪ أغاެني في مجموعتك 🤍 .
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
                    InlineKeyboardButton("تم فتح لوحة 👍🏻 .", callback_data="cbevery"),
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
    f""" - يمديك تشوف اوامر التشغيل تحت .

- شغل | بالرد على ملف صوتي او اسم أغنية

‹ يوت | لتحميل اغنية من اليوتيوب ›

‹ رابط | لحصول رابط الاغنية على اليوتيوب ›

‹ بنك | لفحص سرعة البوت وبنك مللي بالثانية › 

‹ كافي | لايقاف تشغيل جميع الاغاني ›

‹ تج | لتحويل صورة الى رابط تليجراف ›

. شكراً لقرائتك الاوامر - أتمنى لك يوماً تعيساً 🦴 .""",
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
    f""" يمديك تشوف كل اوامر المطورين تحت .

‹ الاحصائيات | لرؤية احصائيات البوت اخر شهر ›

‹ ريستارت | اعادة تشغيل البوت وتحديث المكاتب ›

‹ اذاعة | لعمل اذاعة في المجموعات بدون تثبيت ›

‹ رسالة | لعمل اذاعة لكل المجموعات مع التثبيت ›

‹ المغادرة | لمغادرة حساب المساعد من المجموعات ›

. شكراً لقرائتك الاوامر - أتمنى لك يوماً تعيساً 🦴 .""",
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
    f""" يمديك تشوف كل اوامر المشرفين تحت 🤍 .

‹ كافي | ايقاف تشغيل الاغنية في المجموعة ›

‹ سكب | تخطي التالية الأغنية في المجموعة ›

‹ مؤقتا | لإيقاف تشغيل الأغنية مؤقتا ›

‹ استمر | استمرار التشغيل المتوقف مؤقتا ›

‹ تنظيف | لتنظيف التشغيل وتحسين سرعة البوت ›

‹ ادخل | لدخول حساب المساعد الى المجموعة ›

‹ غادر | لمغادرة حساب المساعد المجموعة ›

. شكراً لقرائتك الاوامر - أتمنى لك يوماً تعيساً 🦴 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ࢪجَۅَعَ", callback_data="cbevery")
                ],
            ]
        ),
    )


# Bot about & Information
@Client.on_callback_query(filters.regex("cbadmins"))
async def admin_set(_, query: CallbackQuery):
    await query.answer("admins menu")
    await query.edit_message_text(
    f"""الحين وصلت الى طريقة تشغيل البوت تحت .

١ | أولا ، أضفني الى مجموعتك
٢ | بعد ذالك قم برفعي كمشرف واعطائي صلاحيات مثل باقي البشر .
٣ | بعد ذالك اكتب تنظيف بيانات البوت
٣ | اضف سيدي ومولاي @{ASSUSERNAME} في مجموعتك او اكتب انضم لدعوة المساعد
٤ | اذ لم تستطيع اضافة المساعد او واجهت مشاكل تحدث مع رئيس الوزراء . @{OWNER_USERNAME}

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("-› ࢪجَۅعَ", callback_data="home_start")
                ],
            ]
        ),
    )
