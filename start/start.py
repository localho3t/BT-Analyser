from app.banner.v1.banner import banner
from app.envChecker.ec import env_check


def starter():
    banner()
    env_check()
