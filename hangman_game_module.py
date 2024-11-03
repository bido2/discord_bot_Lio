from discord import Message

from main import client


def hangman_game():
    @client.event
    async def game_continuation(message: Message):
        user_message: str = message.content
        print(message)