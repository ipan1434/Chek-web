################################################################
"""
 Chek-website jangan hapus credit ngentod gua 
 susah susah but malah hapus credit tolol
 
 @ CREDIT : NOT FOUND 
"""
################################################################
import os
from pyrogram import Client, filters

API_ID = "YOUR_API_ID"  # Ganti dengan API ID Anda
API_HASH = "YOUR_API_HASH"  # Ganti dengan API Hash Anda
BOT_TOKEN = "YOUR_BOT_TOKEN"  # Ganti dengan Token Bot Anda

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Selamat datang! Gunakan /check  untuk memeriksa status website.")

@app.on_message(filters.command("check"))
def check_website(client, message):
    try:
        url = message.command[1]
        response = os.system(f"curl -Is {url} | head -n 1")
        if response == 0:
            message.reply(f"Website {url} berhasil diakses!")
        else:
            message.reply(f"Website {url} tidak dapat diakses.")
    except IndexError:
        message.reply("Silakan masukkan URL setelah perintah /check.")
    except Exception as e:
        message.reply(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    app.run()
