from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 13949344
    API_HASH = "408723003ad67fa8ab01ccc7f53e24ad"
    # the name to display in your alive message
    ALIVE_NAME = "dghfjffsj"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://paccpsmw:aSyVrnhS561v5SJAjeyzJHHDbLvDKiDk@bubble.db.elephantsql.com/paccpsmw"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BJWap1sBuz-IoiI963ChFi48YUFbFE0MM0cTbmKSQNzNa9U01Ggooe6OxsjZc94xC186EPnaQxzvPTz_knSY7iyUBOZdnOXqR7HNUUH0EXnIwCUCunidHnke90vTmdAqJfYOkN1mMVQddh1a0jSFQ_glOtMYh-C1l3OZITBp2D0yHzwXCJW6-zqg4ta3OG_1DCvESe8qbNvDNIbXW0pbLxYMHPBKUJdeYUvp0VXEdYgqMIBWfeRcma2CYB4a1rVK7P6Q5S8188a_Rf5IcZPyJP2shLcgw1djeL6ZCjdp5Ij8UiJWcq5pke5N0b9-MMbCquhGuy8vQ1KlRcRltuLwIOrZ0zRIEpg="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6410048042:AAH5MNKeby7wMB660Zc2yV50QpwtZAjEMm0"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001979159644
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
