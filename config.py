"""
from os import getenv


API_ID = int(getenv("API_ID", "18618422"))
API_HASH = getenv("API_HASH", "f165b1caec3cfa4df943fe1cbe82d22a")
BOT_TOKEN = getenv("BOT_TOKEN", "7064501216:AAEOQMaqLGL5e6TBau-8dYhRxUk5yrG3738")
OWNER_ID = int(getenv("OWNER_ID", "6664582540"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6050277919 2112898623").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002034072106"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002034072106"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", 25318125))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "b29fb6a928e8b8a3308f8c2d3ba9cfb0")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME", "LUCIFEREXTRACTORBOT")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7764674199"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7764674199").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002610898117"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002844381920"))
# -----------------------------♡--------------------------------
#CHANNEL_ID2 = int(os.environ.get("CHANNEL_ID2", "-1002746117621"))
