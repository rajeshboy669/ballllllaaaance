# ©️ DKBOTZ or https://t.me/DKBOTZ
# Coded By https://t.me/DKBOTZHELP 
# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", '1522127')) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", '1252ffe16baf341bfd7236f92df76b0e') #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", '6100205587:AAEN9UfHfOMVfCa7nWW3kNHr-RG3gNCgUeU') # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("5886772061") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", 'cluster0')
DATABASE_URL = os.environ.get("DATABASE_URL", 'mongodb+srv://aaroha:aaroha@cluster0.pnzoc.mongodb.net/Cluster0?retryWrites=true&w=majority&appName=Cluster0') # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", '1006159057')) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1006159057)
#  Optionnal variables
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", '-1002055639714') # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1002055639714") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "True" 


# SHORTNER
SHORT_METHOD = 1 # 2 method added 1 and 2
SHORTNER_LINK = os.environ.get("SHORTNER_LINK", 'npshort.com')
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", 'https://t.me/ANLINKS_IN')
SIMPLE_MODE = os.environ.get("SIMPLE_MODE", False)
