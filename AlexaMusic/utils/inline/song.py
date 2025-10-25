# Copyright (C) 2025 by i_luv_bot @ Github, < https://github.com/pawankrr01 >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/pawankrr01>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import config
from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    return [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌻 sᴜᴩᴩᴏʀᴛ 🌻",
                url=config.SUPPORT_GROUP,
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
