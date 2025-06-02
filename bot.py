################################################################
"""
 Chek-website jangan hapus credit ngentod gua 
 susah susah but malah hapus credit tolol
 
 @ CREDIT : NOT FOUND 
"""
################################################################

from pyrogram import Client, filters
import requests

api_id = "29456099"  # Ganti dengan API ID Anda
api_hash = "34dcbfdfb0eeb9234b8e439fdbef68de"  # Ganti dengan API Hash Anda
bot_token = "7820887672:AAEIm42DMqBSh6w9Id3S0Ls3w1dbhvhssQk"  # Ganti dengan token bot Anda

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Selamat datang! Gunakan /check  untuk memeriksa status website.")

@app.on_message(filters.command("check"))
def check_website(client, message):
    try:
        url = message.command[1]
        response = requests.get(url)
        if response.status_code == 200:
            message.reply(f"Website {url} berhasil diakses!")
        else:
            message.reply(f"Website {url} mengembalikan status: {response.status_code}")
    except Exception as e:
        message.reply(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    app.run()
