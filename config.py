import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "postgres://ojpvryndprsfmv:a86d9638627fd9ba99b330426a1a2ee3921d10acaf4ee05635575d76b7a101df@ec" \
                              "2-34-225-103-117.compute-1.amazonaws.com:5432/d210ga2jq2snmp"
        # os.environ.get("POSTGRE_SQL") or \
        #                       'postgresql://postgres:SNekH2233@localhost:5432/quiz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Testing configuration."""
    # DEBUG = True
    # SQLALCHEMY_DATABASE_URI = ""
    # os.environ.get("POSTGRE_SQL") or \
    #                           'postgresql://postgres:SNekH2233@localhost:5432/quiz_test'
