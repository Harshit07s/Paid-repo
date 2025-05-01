
import os

import logging

from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton





TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7718124664:AAHMHtKEAkX_Qy3l9m7AxsujhkUFOLPXVes")



#Your API ID from my.telegram.org

API_ID = int(os.environ.get("API_ID", "29803966"))



#Your API Hash from my.telegram.org

API_HASH = os.environ.get("API_HASH", "58d51659fe8038960a3db77d6e2c4265")



#Your db channel Id

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002526544378"))



#OWNER ID

OWNER_ID = int(os.environ.get("OWNER_ID", "879520667"))



#Port

PORT = os.environ.get("PORT", "8036")



DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://rohitplayer87089:rohit870@cluster0.4wt927p.mongodb.net/?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DATABASE_NAME", "mendak")









IS_VERIFY = os.environ.get("IS_VERIFY", "True")

TUT_VID = os.environ.get("TUT_VID", "https://t.me/+75lYowcxb8dhZDk0")







TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "100"))



START_PIC = os.environ.get("START_PIC", "https://envs.sh/Nr_.jpg")

FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/Nr_.jpg")



QR_PIC = os.environ.get("QR_PIC", "https://envs.sh/i-v.jpg")









#set your Custom Caption here, Keep None for Disable Custom Caption

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>@KM_PORTAL @SINSFULL_BOT</b>")



#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links

PICS = (os.environ.get("PICS", "https://envs.sh/4Iq.jpg https://envs.sh/4IW.jpg https://envs.sh/4IB.jpg https://envs.sh/4In.jpg")).split() #Required







#==========================(BUY PREMIUM)====================#



PREMIUM_BUTTON = reply_markup=InlineKeyboardMarkup(

        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]

)



PREMIUM_BUTTON2 = reply_markup=InlineKeyboardMarkup(

        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]

) 



OWNER_TAG = os.environ.get("OWNER_TAG", "LORDLEAKS_BOT")



#UPI ID

UPI_ID = os.environ.get("UPI_ID", "moneypaglu@jio")



#UPI QR CODE IMAGE

UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://t.me/paymentofsnaps/5")



#SCREENSHOT URL of ADMIN for verification of payments

SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", "t.me/lordleaks_bot")







#Time and its price



#7 Days

PRICE1 = os.environ.get("PRICE1", "40 rs")



#1 Month

PRICE2 = os.environ.get("PRICE2", "100 rs")



#3 Month

PRICE3 = os.environ.get("PRICE3", "250 rs")



#6 Month

PRICE4 = os.environ.get("PRICE4", "500 rs")



#1 Year

PRICE5 = os.environ.get("PRICE5", "900 rs")





#===================(END)========================#





#Set true if you want Disable your Channel Posts Share button

DISABLE_CHANNEL_BUTTON = os.environ.get("True", True) == 'False'



BOT_STATS_TEXT = "<b>BOT UPTIME🔥</b>\n{uptime}"

USER_REPLY_TEXT = "âŒDon't send me messages directly I'm only File Sharing Bot! By @km_portal"









LOG_FILE_NAME = "filesharingbot.txt"



logging.basicConfig(

    level=logging.INFO,

    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",

    datefmt='%d-%b-%y %H:%M:%S',

    handlers=[

        RotatingFileHandler(

            LOG_FILE_NAME,

            maxBytes=50000000,

            backupCount=10

        ),

        logging.StreamHandler()

    ]

)

logging.getLogger("pyrogram").setLevel(logging.WARNING)





def LOGGER(name: str) -> logging.Logger:

    return logging.getLogger(name)
