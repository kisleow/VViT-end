from starlette.config import Config

config = Config(".env")

TOKEN: str = config("TOKEN")
DATABASE: str = config("DATABASE")
USER: str = config("USER")
PASSWORD: str = config("PASSWORD")
