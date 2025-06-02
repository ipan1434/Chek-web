################################################################
"""
 Chek-website jangan hapus credit ngentod gua 
 susah susah but malah hapus credit tolol
 
 @ CREDIT : NOT FOUND 
"""
################################################################

from pyrogram import Client, filters

# Ganti dengan token bot Anda
API_ID = '29456099'
API_HASH = '34dcbfdfb0eeb9234b8e439fdbef68de'
BOT_TOKEN = '7820887672:AAEIm42DMqBSh6w9Id3S0Ls3w1dbhvhssQk'

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply("Selamat datang! Gunakan /check  untuk memeriksa status website.")

@app.on_message(filters.command("check"))
def check_command(client, message):
    try:
        url = message.command[1]
        response = requests.get(url)
        status_code = response.status_code
        message.reply(f"Status website {url}: {status_code}")
    except IndexError:
        message.reply("Silakan masukkan URL setelah perintah /check.")
    except Exception as e:
        message.reply(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    app.run()
