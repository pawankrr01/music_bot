# Copyright (C) 2025 by i_luv_bot @ Github, < https://github.com/pawankrr01 >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/pawankrr01>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from typing import Dict, List, Union

from AlexaMusic.core.mongo import mongodb


onoffdb = mongodb.onoffper


async def is_on_off(on_off: int) -> bool:
    onoff = await onoffdb.find_one({"on_off": on_off})
    return bool(onoff)


async def add_on(on_off: int):
    is_on = await is_on_off(on_off)
    if is_on:
        return
    return await onoffdb.insert_one({"on_off": on_off})


async def add_off(on_off: int):
    is_off = await is_on_off(on_off)
    if not is_off:
        return
    return await onoffdb.delete_one({"on_off": on_off})
