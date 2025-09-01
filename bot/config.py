import os


class Config:

    BOT_TOKEN = os.environ.get("7627011309:AAHf2txD-WsYk--0-oX3s0XKDWDnqurub6w")

    SESSION_NAME = os.environ.get("SameerTxt2_X_Bot", ":memory:")

    API_ID = int(os.environ.get("29755489"))

    API_HASH = os.environ.get("05e0d957751c827aa03494f503ab54fe")

    CLIENT_ID = os.environ.get("1052835451975-h52kcf7othp25bovih9h7btvkpm6dreq.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("6624738128"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
