import os
from http.client import responses
from typing import Final
from dotenv import  load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#Loading discord token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

async def send_message(message: Message, user_Message) -> str:
    if not user_Message:
        print('empty message')
        return

    if is_private := user_Message[0] == '\'':
        user_Message = user_Message[1:]

    try:
        response: str = get_response(user_Message)
        await message.author.send(response) if is_private else message.channel.send(response)
    except Exception as e:
        print(e)
