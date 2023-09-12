from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 14263311
    API_HASH = "c66911c3000c82abc7f41566520ae42c"
    # the name to display in your alive message
    ALIVE_NAME = "amirbeee007maoo"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://mhmlbosd:RlXLtCNSw0ZlDyrsf3bjms2JZUYrBjip@bubble.db.elephantsql.com/mhmlbosd"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BJWap1sBuwGPRlfxEyI2s4LYCk7qEHvymPk3iGXObwE5ajXFBX6wIHdzxmv0qP14jhqbOpXaaELdGBVSvUzYTbF1275Ju5BcXGCjZW4GByKryMW0jprNvkElAE851KKeCH4GITSytI9Sd9alL4kpogqmxwncPcXu7G4xpPmrLOrQqLwOeUYb9hO0d58PgG_6zjRinY9ltHC0Uh74UutpcxzuMEhxj_veIzCwjUZ1NArMgHbiSOvs9fsMkJq1brjHDDi4964xJ2LTE__Su41mZeCzIN_9uHGow4gg1Ld_6o9xMZVztjN6AHSEsIuxdGHSnlO9PrGuv0NfBQTKNB0X0Hsf-AB8igs="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6682529432:AAEqFocdqOoy3kB4qSkevxebvs9x14gAeKc"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001861207760
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
