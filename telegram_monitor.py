from telethon.sync import TelegramClient, events
import requests

api_id = 20295619
api_hash = "1f7150b62cc6f2cf1c38f0855719272c"
channel_username = "@PocketOptionSignalsM5"
webhook_url = "https://marisbriedis.app.n8n.cloud/webhook/b0ba3ab9-cec8-4eee-b404-8e276ac6965a"

win_streak = 0
streak_target = 2

client = TelegramClient('user_session', api_id, api_hash)

# Safe connection for headless environments
client.connect()
if not client.is_user_authorized():
    raise Exception("Session file missing or expired. Please run locally to sign in once.")

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    global win_streak

    raw_text = event.message.message.strip()
    message_text = raw_text.lower()
    print(f"📩 New message received:\n{raw_text}\n")

    if message_text == "win ✅":
        win_streak += 1
        print(f"[+]{win_streak} consecutive WINs")
    else:
        if win_streak > 0:
            print(f"[-] Streak broken at {win_streak}")
        win_streak = 0

    if win_streak == streak_target:
        print("🔥 2 WINs in a row detected! Sending webhook…")
        try:
            requests.post(webhook_url, json={"message": "2 consecutive WINs detected!"})
            print("✅ Webhook sent.")
        except Exception as e:
            print("❌ Webhook failed:", str(e))
        win_streak = 0

print("📡 Listening for messages...")
client.run_until_disconnected()
