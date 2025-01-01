from pyrogram.types import InlineKeyboardButton

import config
from MOON_MUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_3"],url=f"https://t.me/{app.username}?startgroup=true",)
        ],

        [
            InlineKeyboardButton(text=_["S_B_10"], callback_data="HELP_ABOUT"),
            InlineKeyboardButton(text=_["˹ ᴧʙσυт ˼"], callback_data="MAIN_CP"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
       
    ]
    return buttons