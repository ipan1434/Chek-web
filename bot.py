from pyrogram import Client, filters
import requests

# Ganti 'YOUR_API_ID' dan 'YOUR_API_HASH' dengan nilai yang sesuai
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("welcome silahkan kirim link anda untuk di chek apa lah ke DDoS atau tidak")

@app.on_message(filters.text)
def check_website(client, message):
    url = message.text
    try:
        response = requests.get(url)
        if response.status_code == 200:
            message.reply(f"Website {url} sedang online!")
        else:
            message.reply(f"Website {url} tidak dapat diakses. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        message.reply(f"Terjadi kesalahan saat mengakses {url}: {e}")

app.run()
