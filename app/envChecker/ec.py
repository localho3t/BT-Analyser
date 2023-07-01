import os


def env_check():
    if os.path.exists(".env"):
        print("Env Exists")
    else:
        from app.envChecker.create_env import create
        create()
