import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "postgres://ykmvnilovrians:73455fbed68cdb6ab18480b5859c2df166d64c9cc287fde4d5316b97cc24e6fd@ec2-34-225-103-117.compute-1.amazonaws.com:5432/deeobjoq68qpfb"
        # os.environ.get("POSTGRE_SQL") or \
        #                       'postgresql://postgres:SNekH2233@localhost:5432/quiz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Testing configuration."""
    # DEBUG = True
    # SQLALCHEMY_DATABASE_URI = ""
    # os.environ.get("POSTGRE_SQL") or \
    #                           'postgresql://postgres:SNekH2233@localhost:5432/quiz_test'
