#!/usr/bin/env python
import os

from typing import Any

import discord

client = discord.Client()


def get_actions_environ(
    key: str, default_value: Any = None, required: bool = False
) -> Any:
    if key in os.environ:
        return os.environ[key]
    elif f"INPUT_{key.upper()}" in os.environ:
        return os.environ[f"INPUT_{key.upper()}"]
    elif required:
        raise KeyError(f"{key} not found in environment.")

    return default_value


async def message_or_update():
    channel = client.get_channel(
        int(get_actions_environ("DISCORD_CHANNEL", required=True))
    )
    message_id = get_actions_environ("DISCORD_MESSAGE", channel.last_message_id)

    message_file_path = get_actions_environ("MESSAGE_FILE", "/etc/discord-message-updater/message")
    with open(message_file_path) as message_file:
        message = message_file.read()

    if message_id and message_id != "new":
        discord_message = await channel.fetch_message(message_id)
        await discord_message.edit(content=message)
    else:
        await channel.send(content=message)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await message_or_update()
    await client.logout()
    
print(f"Token: ")
print(get_actions_environ("DISCORD_TOKEN", required=True))
client.run(get_actions_environ("DISCORD_TOKEN", required=True))
