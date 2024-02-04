import os

from passlib.context import CryptContext


class Environment:
    """Helper class to get environment variables"""

    @classmethod
    def get_string(cls, config_name, default=""):
        return str(os.getenv(config_name, default))


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)