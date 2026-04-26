import os
import time

from .input_data_validations import sanitize_env_var


def get_unix_epoch_now() -> int:
    unix_epoch_now = int(time.time() * 1000)
    return unix_epoch_now


def get_autograder_safe_genre(genre: str) -> str:
    # Autograder has a weird behaivor where it expects the genre value to be
    # integer and not string if the value only consists of integers.
    genre = str(genre)
    if genre.isnumeric():
        genre = float(genre)
        if genre.is_integer():
            genre = int(genre)
    return genre


def get_is_valid_keyword(keyword: str) -> bool:
    keyword = str(keyword)
    for c in keyword:
        if not c.isalpha():
            return False
    return True


def get_env_vars_for_api_service_books_commands():
    IS_DEV = os.environ.get("IS_DEV", None)
    IS_DEV = True if IS_DEV is not None else False
    print(f"[INFO] IS_DEV = {IS_DEV}")

    DB_USER = os.environ.get("DB_USER", None)
    DB_PASS = os.environ.get("DB_PASS", None)
    DB_URL = os.environ.get("DB_URL", None)
    DB_PORT = os.environ.get("DB_PORT", None)
    DB_DATABASE = os.environ.get("DB_DATABASE", None)
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", None)
    should_raise_exception = False
    if DB_USER is None:
        print("[ERROR] DB_USER = None")
        should_raise_exception = True
    if DB_PASS is None:
        print("[ERROR] DB_PASS = None")
        should_raise_exception = True
    if DB_URL is None:
        print("[ERROR] DB_URL = None")
        should_raise_exception = True
    if DB_PORT is None:
        print("[ERROR] DB_PORT = None")
        should_raise_exception = True
    if DB_DATABASE is None:
        print("[ERROR] DB_DATABASE = None")
        should_raise_exception = True
    if GEMINI_API_KEY is None:
        print("[ERROR] GEMINI_API_KEY = None")
        should_raise_exception = True
    if should_raise_exception:
        raise Exception(
            "[ERROR] Required credentials were not found in the environment variables"
        )

    # K8s includes something like DB_USER='...' to include the quotes themselves too.
    # Thus, sanitize it so that the env vars do not start with or end with quotes.
    DB_USER = sanitize_env_var(DB_USER)
    DB_PASS = sanitize_env_var(DB_PASS)
    DB_URL = sanitize_env_var(DB_URL)
    DB_PORT = int(float(sanitize_env_var(DB_PORT)))
    DB_DATABASE = sanitize_env_var(DB_DATABASE)
    GEMINI_API_KEY = sanitize_env_var(GEMINI_API_KEY)

    return (IS_DEV, DB_USER, DB_PASS, DB_URL, DB_PORT, DB_DATABASE, GEMINI_API_KEY)


def get_env_vars_for_api_service_books_queries():
    IS_DEV = os.environ.get("IS_DEV", None)
    IS_DEV = True if IS_DEV is not None else False
    print(f"[INFO] IS_DEV = {IS_DEV}")

    DB_USER = os.environ.get("DB_USER", None)
    DB_PASS = os.environ.get("DB_PASS", None)
    DB_URL = os.environ.get("DB_URL", None)
    DB_PORT = os.environ.get("DB_PORT", None)
    DB_DATABASE = os.environ.get("DB_DATABASE", None)
    DB_COLLECTION = os.environ.get("DB_COLLECTION", None)
    API_RELATED_BOOKS_URL = os.environ.get("API_RELATED_BOOKS_URL", None)
    should_raise_exception = False
    if DB_USER is None:
        print("[ERROR] DB_USER = None")
        should_raise_exception = True
    if DB_PASS is None:
        print("[ERROR] DB_PASS = None")
        should_raise_exception = True
    if DB_URL is None:
        print("[ERROR] DB_URL = None")
        should_raise_exception = True
    # In prod, a MongoDB cluster is used instead of a local instance of MongoDB.
    # MongoDB clusters don't accept port numbers.
    if DB_PORT is None and IS_DEV:
        print("[ERROR] DB_PORT = None")
        should_raise_exception = True
    if DB_DATABASE is None:
        print("[ERROR] DB_DATABASE = None")
        should_raise_exception = True
    if DB_COLLECTION is None:
        print("[ERROR] DB_COLLECTION = None")
        should_raise_exception = True
    if API_RELATED_BOOKS_URL is None:
        print("[ERROR] API_RELATED_BOOKS_URL = None")
        should_raise_exception = True
    if should_raise_exception:
        raise Exception(
            "[ERROR] Required credentials were not found in the environment variables"
        )

    # K8s includes something like DB_USER='...' to include the quotes themselves too.
    # Thus, sanitize it so that the env vars do not start with or end with quotes.
    DB_USER = sanitize_env_var(DB_USER)
    DB_PASS = sanitize_env_var(DB_PASS)
    DB_URL = sanitize_env_var(DB_URL)
    DB_PORT = int(float(sanitize_env_var(DB_PORT))) if IS_DEV else None
    DB_DATABASE = sanitize_env_var(DB_DATABASE)
    DB_COLLECTION = sanitize_env_var(DB_COLLECTION)
    API_RELATED_BOOKS_URL = sanitize_env_var(API_RELATED_BOOKS_URL)

    return (
        IS_DEV,
        DB_USER,
        DB_PASS,
        DB_URL,
        DB_PORT,
        DB_DATABASE,
        DB_COLLECTION,
        API_RELATED_BOOKS_URL,
    )
