#Github.com/mrinvisible7

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "26075120"
API_HASH = "1fda88a5d1de46058a4791c78bce198e"
BOT_TOKEN = "6252974770:AAHkofRqdOs4PI7ITJQXzlg68qKjQcgPEoA"
SESSION = "BQGTAMIAku6i8xI9m8E4YVxwmOuMBsVo8zKoz_Dr4cCXkR8DG9RkNQbSR3Vk93vNul_mm1dq5KBcgOFLvmLOFy9wvOrp9vWVmyrnQRKc8V74W-MZjIfkrSXPVUWkuUahd2dcwHA0FnQ-sLWJJ_lxIsUvHU_MZpc80Q0yEcQWbWQT9Fql9pM0JU21opkxHs3odM8GKJxpLZmKn_w_Ft2OA9OMjuTQxo18QtA0c5KML1UkuNU-7QMKQoKxHX45sW_dJLI24UsVQAutWt6it9HqblbG4zhhFbl5fHA3fkE0h6U8ejkwkXiHBfh0OG-jQJSdb7-Pimv2OM_Y3uWKXa-P-yrRkCNa7AAAAAGQxkeQAA"
FORCESUB = "stringsessionAK47"
AUTH = "6723880848"
SUDO_USERS = []
if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
