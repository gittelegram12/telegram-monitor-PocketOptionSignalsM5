from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 20295619
api_hash = "1f7150b62cc6f2cf1c38f0855719272c"  # use your real one

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your string session:\n")
    print(client.session.save())
