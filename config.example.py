class DebugConfig:
    db_host = "127.0.0.1"
    db_user = "root"
    db_pw = ""
    db_name = "riega_tu_planta"

    SECRET_KEY = "P4$$W0rDS3cr3T"

    SQLALCHEMY_DATABASE_URI = f'mysql://{db_user}:{db_pw}@{db_host}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class ProdConfig:
    db_host = "127.0.0.1"
    db_user = "root"
    db_pw = ""
    db_name = "riega_tu_planta"

    SECRET_KEY = "P4$$W0rDS3cr3T"

    SQLALCHEMY_DATABASE_URI = f'mysql://{db_user}:{db_pw}@{db_host}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False
