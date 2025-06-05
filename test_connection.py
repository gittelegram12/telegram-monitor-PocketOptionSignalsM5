from telethon.sync import TelegramClient

api_id = 20295619
api_hash = "a1b2c3d4e5f6g7h8i9j0"

with TelegramClient('test_session', api_id, api_hash) as client:
    me = client.get_me()
    print(me.username)
