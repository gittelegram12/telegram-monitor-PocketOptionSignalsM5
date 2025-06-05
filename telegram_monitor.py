from telethon.sync import TelegramClient, events
import requests

api_id = "20295619"
api_hash = "1f7150b62cc6f2cf1c38f0855719272c"
channel_username = "@baazigarn8n_bot"
webhook_url = "https://marisbriedis.app.n8n.cloud/webhook-test/accada36-9029-4db0-88d6-23b02bec865d"

client = TelegramClient('user_session', api_id, api_hash)
client.start()

# Pattern tracking
sequence = []

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    global sequence

    message_text = event.message.message.lower().strip()
    print(f"📨 New message: {message_text}")

    if "win ✅" in message_text:
        sequence.append("win")
        print("✅ Detected: WIN")
    else:
        sequence.append("call")
        print("📈 Detected: SIGNAL CALL")

    # Keep only the last 4 elements
    if len(sequence) > 4:
        sequence.pop(0)

    # Check for pattern: call → win → call → win
    if sequence == ["call", "win", "call", "win"]:
        print("🔥 Detected 2 consecutive SIGNAL → WIN pairs. Sending webhook...")
        try:
            requests.post(webhook_url, json={"message": "2 consecutive trading wins detected!"})
            print("✅ Webhook sent.")
        except Exception as e:
            print("❌ Webhook failed:", str(e))
        sequence = []  # Reset sequence after webhook

print("📡 Listening for messages...")
client.run_until_disconnected()
