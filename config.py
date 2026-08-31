"""Configuration loaded from environment variables.

Never hard-code secrets in source files: anything committed to a public
repository is public forever, even after you delete it.

Usage:
    cp .env.example .env      # then fill in the real values
"""
import os

from dotenv import load_dotenv

load_dotenv()


def _required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"{name} is not set. Copy .env.example to .env and fill it in."
        )
    return value


BOT_TOKEN = _required("BOT_TOKEN")

# Backwards-compatible alias for the original module-level name.
TOKEN = BOT_TOKEN

TOKEN = '7123114183:AAEA5CvPSDkYdNBl0my5lrj3sXBt_Zl8P-I'


TOKEN = 'YOR TOKEN'
