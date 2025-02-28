from os import environ

API_ID = int(environ.get("API_ID", "20496814"))
API_HASH = environ.get("API_HASH", "a87c1094edd18650e5dfee0f2bc78bda")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002321506152"))
ADMINS = int(environ.get("ADMINS", "6276113288"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "nhmovies9")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
