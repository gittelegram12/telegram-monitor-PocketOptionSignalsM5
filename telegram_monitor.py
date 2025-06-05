from telethon.sync import TelegramClient, events
import os
import requests

api_id = 20295619
api_hash = "a1b2c3d4e5f6g7h8i9j0"
channel_username = "@PocketSignalsM1"
webhook_url = "https://marisbriedis.app.n8n.cloud/webhook/b0ba3ab9-cec8-4eee-b404-8e276ac6965a"

win_streak = 0
streak_target = 5

client = TelegramClient('win_monitor_session', api_id, api_hash)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    global win_streak

    message_text = event.message.message.lower()
    if "win" in message_text:
        win_streak += 1
        print(f"[+]{win_streak} consecutive WINs")
    else:
        if win_streak > 0:
            print(f"[-] Streak broken at {win_streak}")
        win_streak = 0

    if win_streak == streak_target:
        print("🔥 5 WINs in a row detected! Sending webhook…")
        try:
            requests.post(webhook_url, json={"message": "5 consecutive WINs detected!"})
            print("✅ Webhook sent.")
        except Exception as e:
            print("❌ Webhook failed:", str(e))
        win_streak = 0  # reset after notification

print("📡 Listening for messages...")
client.start()
client.run_until_disconnected()
