import random 
from pyrogram import filters, Client
from pyrogram.types import Message
from folder.config import SUDO_USERS
from tool.cache.data import RAID
from tool.sos.help import *

REPLY = (
    "Jaa na Bsdk, gaand mara jaake.",
    "Tu paidaishi chutiya hai ki koi course kiya hai? ",
    "randi chod ke 1/- me apni gand bech le",
    "lode pe lagi hai haldi chuss mere jaildi",
    "And the truth is, you're a fucking cunt",
    "Bohot Sari RANDI dekhi lakin teri chut sabse aalag",
    "Jaa na Gandu",
    "Aand ka na Gaand ka, Gyaan jhaare pure Brahmand ka",
    "Dhaat teri maa ki ch*t",
    "Gaand se tatti nikalke jaadugar samajhta hai apne aap ko?",
    "kitne me bechaga😆",
    "izzat karo humari warna maa chod denge tumari",
    "Tu aise nhi maanega - Mat maan, maa chuda",
    "Tujhse zada sundar teri jali hui gaand hai",
    "Ye aapki Randikhana nhi hai, kripya yaha se dur rahe",
    "Madarchod sunn PANI KAAM HAI MATKE ME GAND MAAR LUNGA EAK JATKE ME",
    "Sun randi chod..Ja ke gand mara aur baap banne ki kushi de...kisi ko, yaha backchodi naa paal",
    "Tere jaise badawe Bohot milte hai Bosari chod ke nikal le yaha se",
    "Wahhh Bato to kitna MADARchod BETA HAI MERE baap ki izzat tak nahi karta🥲",
    "abee o nibba Lodi den ki Abhi nibbi ke sath transgender wali harkate krr yaha abhi chako walii harkate naa kr",
    "Wahh behencooo Teri kitni mast hai 🤤aur eak baar chodne de🤤",
    "Andi mandi randi teri jaisa bohot hai yaha randi",
    "Teri baap ne bina lode ke tere ko kaise paida kiya🤔\nOHHH haa teri maa to randi hai😆",
    "Chutiye nikal apni chut ka pardashan kahi aur krr",
    "Sun bete aand kitne be bade kyu na ho jaye rehete Lodee ke niche he hai 😆iss liya zada na udd",
    "Sale zada na boll warna apne lund ki eak ke saat se lodu muu me chipka dunga phir mere loda apne muu me le kr gumna 😆",
    "Bohot randi chod ke dekhe lakin tu sabse bada wala hai🤣",
    "kitno se marawa marawa ke apni khuli kara li hai 😆",
    "Its Silent Lovish here,...\ni don't abuse lakin tum MADARchod ho🙂",
    "kyaa be behenchod",
    "gand naa mataka free me jonny bhiya ko de dunga😆aage ka dekh lena😆",
    "Bsdk tameej s bola kr wrna teri gaand m dnda ghusana mne",
    "Abe gaandu insaan teri maa ko na nanga krke chodna",
    "bc gaand Or chut m ek sth ghusana saali randi do kodi ki",
    "Wrna khade khade gaand m dnda ghusa k muh s bhr nikalungi",
    "Bhosdike tune 2nd hand randi ko pela hoga....aya bada baap ko sikhane",
    "gaand main ek baal nhi apni chudi hui gaand leke chale aata hai bhosdika",
    "Lund bhi hai terepass?? Lund hoga bhi kaise!! Tu to Chakka hai!!",
    "Lulli Khadi bhi Hoti hai teri?? Abe yaar bhul gya tha teri to lulli hi hai nhi!!",
    "Maa chuda le apni jaa ke😂",
    "Apni maa ki maar jor s jb chillayegi na tb chlega pta",
    "Randi teri jaisi bohot dekhi hai ladwe pe charna chati hai sirf",
    "Tera lawda mne tere muh m ghusana h randi ki aulad",
    "Muu me le mere ladwa",
    "Gand mara aur condom ke karu yaa bina condom ke kon sa flavour legi😂",
    "Samjha Tera Baap sirf main hun....Teri randi maa ko maine choda tha😂😂...tu mere sperm se paida hua hai MC....",
    "tu to MC kehlane ke liye layak bhi nhi luli jo nhi hai",
    "abe chutiya behench****",
    "Behen ke lode madahrchod teri ma randi bhsdk tera pyra khandan randi",
    "MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI ",
    "DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN ladata hai chutiye",
    "gaye ke piche pada hai sannd tere jaise mere niche latak rehe hai do aand",
    "Teri maan ko itna chodu gha na ki wo chila chila ke thak jayagi🥲",
    "Tere jaise bacho se liye 3 puri raat gand mari wo be liye cheen",
    "Pani kaam hai bottle me gand marunga teri hotel me😂"
    )

@Client.on_message(filters.command(["abuse", "gali"], ".") & filters.me)
async def abuse(client: Client, msg: Message): 
        await msg.edit(random.choice(RAID))



add_command_help(
    "Abuse",
    [
        [".abuse", "To Abuse Someone !!"],
    ],
)


from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import *
from pyrogram import Client
from tool.sos.help import *

ALIVE_PIC = " "
 

 
@Client.on_message(filters.command(["alive", "awake", "ping"], [".", "!"]) & filters.me)
async def alive(client: Client, e: Message):
    ids = 0
    try:
        if bot:
            ids += 1
        if bot1:
            ids += 1
        if bot2:
            ids += 1
        if bot3:
            ids += 1
        if bot4:
            ids += 1
        if bot5:
            ids += 1
        if bot6:
            ids += 1
        if bot7:
            ids += 1
        if bot8:
            ids += 1
        if bot9:
            ids += 1
        if bot:
            ids += 1
        if bot11:
            ids += 1
        if bot12:
            ids += 1
        if bot13:
            ids += 1
        if bot14:
            ids += 1
        if bot15:
            ids += 1
        if bot16:
            ids += 1
        if bot17:
            ids += 1
        if bot18:
            ids += 1
        if bot19:
            ids += 1
        if bot20:
            ids += 1
        if bot21:
            ids += 1
        if bot22:
            ids += 1
        if bot23:
            ids += 1
        if bot24:
            ids += 1
        if bot25:
            ids += 1
        if bot26:
            ids += 1
        if bot27:
            ids += 1
        if bot28:
            ids += 1
        if bot29:
            ids += 1
        if bot30:
            ids += 1
        if bot31:
            ids += 1
        if bot32:
            ids += 1
        if bot33:
            ids += 1
        if bot34:
            ids += 1
        if bot35:
            ids += 1
        if bot36:
            ids += 1
        if bot37:
            ids += 1
        if bot38:
            ids += 1
        if bot39:
            ids += 1
        if bot40:
            ids += 1
        if bot41:
            ids += 1
        if bot42:
            ids += 1
        if bot43:
            ids += 1
        if bot44:
            ids += 1
        if bot45:
            ids += 1
        if bot46:
            ids += 1
        if bot47:
            ids += 1
        if bot48:
            ids += 1
        if bot49:
            ids += 1
        if bot50:
            ids += 1
        Alive_msg = f"**🌟 Inflex M8N ToolKit 🌟**\n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► version : `Beta.0.1` \n"
        Alive_msg += f"► pyrogram : `{pyro_vr}` \n"
        Alive_msg += f"► Active Ids : `{ids}` \n"
        Alive_msg += f"► Help : [Join Here](https://t.me/M8N_SUPPORT) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "🌐 Channel", url="https://t.me/M8N_OFFICIAL")
                ], [
                    InlineKeyboardButton(
                        "🚀 Repo", url="https://github.com/UnknownMortal/Tool")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"**🌟 Inflex M8N ToolKit 🌟**\n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► version : `Beta.0.1` \n"
        Alive_msg += f"► pyrogram : `1.4.15` \n"
        Alive_msg += f"► support : [Join Here](https://t.me/M8N_SUPPORT) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🌐 Channel", url="https://t.me/M8N_OFFICIAL"),
                ],
                [
                    InlineKeyboardButton("🚀 Repo", url="https://github.com/UnknownMortal/Tool"),
                ],
            ],
        ),
    ) 

add_command_help(
    "ping",
    [
        [
            ".ping",
            "This Command for check your bot working or not !!",
        ]
    ],
)
