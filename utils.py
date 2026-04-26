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

    DB_URL = os.environ.get("DB_URL", None)
    DB_PORT = os.environ.get("DB_PORT", None)
    DB_USER = os.environ.get("DB_USER", None)
    DB_PASS = os.environ.get("DB_PASS", None)
    DB_DATABASE = os.environ.get("DB_DATABASE", None)
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", None)
    should_raise_exception = False
    if DB_URL is None:
        print("[ERROR] DB_URL = None")
        should_raise_exception = True
    if DB_PORT is None:
        print("[ERROR] DB_PORT = None")
        should_raise_exception = True
    if DB_USER is None:
        print("[ERROR] DB_USER = None")
        should_raise_exception = True
    if DB_PASS is None:
        print("[ERROR] DB_PASS = None")
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
    DB_URL = sanitize_env_var(DB_URL)
    DB_PORT = int(float(sanitize_env_var(DB_PORT)))
    DB_USER = sanitize_env_var(DB_USER)
    DB_PASS = sanitize_env_var(DB_PASS)
    DB_DATABASE = sanitize_env_var(DB_DATABASE)
    GEMINI_API_KEY = sanitize_env_var(GEMINI_API_KEY)

    CONFIGS = {
        IS_DEV: IS_DEV,
        DB_URL: DB_URL,
        DB_PORT: DB_PORT,
        DB_USER: DB_USER,
        DB_PASS: DB_PASS,
        DB_DATABASE: DB_DATABASE,
        GEMINI_API_KEY: GEMINI_API_KEY,
    }
    return CONFIGS


def get_env_vars_for_api_service_books_queries():
    IS_DEV = os.environ.get("IS_DEV", None)
    IS_DEV = True if IS_DEV is not None else False
    print(f"[INFO] IS_DEV = {IS_DEV}")

    DB_URL = os.environ.get("DB_URL", None)
    DB_PORT = os.environ.get("DB_PORT", None)
    DB_USER = os.environ.get("DB_USER", None)
    DB_PASS = os.environ.get("DB_PASS", None)
    DB_DATABASE = os.environ.get("DB_DATABASE", None)
    DB_COLLECTION = os.environ.get("DB_COLLECTION", None)
    API_RELATED_BOOKS_URL = os.environ.get("API_RELATED_BOOKS_URL", None)
    should_raise_exception = False
    if DB_URL is None:
        print("[ERROR] DB_URL = None")
        should_raise_exception = True
    # In prod, a MongoDB cluster is used instead of a local instance of MongoDB.
    # MongoDB clusters don't accept port numbers.
    if DB_PORT is None and IS_DEV:
        print("[ERROR] DB_PORT = None")
        should_raise_exception = True
    if DB_USER is None:
        print("[ERROR] DB_USER = None")
        should_raise_exception = True
    if DB_PASS is None:
        print("[ERROR] DB_PASS = None")
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
    DB_URL = sanitize_env_var(DB_URL)
    DB_PORT = int(float(sanitize_env_var(DB_PORT))) if IS_DEV else None
    DB_USER = sanitize_env_var(DB_USER)
    DB_PASS = sanitize_env_var(DB_PASS)
    DB_DATABASE = sanitize_env_var(DB_DATABASE)
    DB_COLLECTION = sanitize_env_var(DB_COLLECTION)
    API_RELATED_BOOKS_URL = sanitize_env_var(API_RELATED_BOOKS_URL)

    CONFIGS = {
        IS_DEV: IS_DEV,
        DB_URL: DB_URL,
        DB_PORT: DB_PORT,
        DB_USER: DB_USER,
        DB_PASS: DB_PASS,
        DB_DATABASE: DB_DATABASE,
        DB_COLLECTION: DB_COLLECTION,
        API_RELATED_BOOKS_URL: API_RELATED_BOOKS_URL,
    }
    return CONFIGS


def get_env_vars_for_cronjob_sync_data():
    IS_DEV = os.environ.get("IS_DEV", None)
    IS_DEV = True if IS_DEV is not None else False
    print(f"[INFO] IS_DEV = {IS_DEV}")

    DB_BOOKS_COMMANDS_URL = os.environ.get("DB_BOOKS_COMMANDS_URL", None)
    DB_BOOKS_COMMANDS_PORT = os.environ.get("DB_BOOKS_COMMANDS_PORT", None)
    DB_BOOKS_COMMANDS_USER = os.environ.get("DB_BOOKS_COMMANDS_USER", None)
    DB_BOOKS_COMMANDS_PASS = os.environ.get("DB_BOOKS_COMMANDS_PASS", None)
    DB_BOOKS_COMMANDS_DATABASE = os.environ.get("DB_BOOKS_COMMANDS_DATABASE", None)
    should_raise_exception = False
    if DB_BOOKS_COMMANDS_URL is None:
        print("[ERROR] DB_BOOKS_COMMANDS_URL = None")
        should_raise_exception = True
    if DB_BOOKS_COMMANDS_PORT is None:
        print("[ERROR] DB_BOOKS_COMMANDS_PORT = None")
        should_raise_exception = True
    if DB_BOOKS_COMMANDS_USER is None:
        print("[ERROR] DB_BOOKS_COMMANDS_USER = None")
        should_raise_exception = True
    if DB_BOOKS_COMMANDS_PASS is None:
        print("[ERROR] DB_BOOKS_COMMANDS_PASS = None")
        should_raise_exception = True
    if DB_BOOKS_COMMANDS_DATABASE is None:
        print("[ERROR] DB_BOOKS_COMMANDS_DATABASE = None")
        should_raise_exception = True
    if should_raise_exception:
        raise Exception(
            "[ERROR] Required credentials were not found in the environment variables"
        )

    # K8s includes something like DB_BOOKS_COMMANDS_USER='...' to include the quotes themselves too.
    # Thus, sanitize it so that the env vars do not start with or end with quotes.
    DB_BOOKS_COMMANDS_URL = sanitize_env_var(DB_BOOKS_COMMANDS_URL)
    DB_BOOKS_COMMANDS_PORT = int(float(sanitize_env_var(DB_BOOKS_COMMANDS_PORT)))
    DB_BOOKS_COMMANDS_USER = sanitize_env_var(DB_BOOKS_COMMANDS_USER)
    DB_BOOKS_COMMANDS_PASS = sanitize_env_var(DB_BOOKS_COMMANDS_PASS)
    DB_BOOKS_COMMANDS_DATABASE = sanitize_env_var(DB_BOOKS_COMMANDS_DATABASE)

    DB_BOOKS_QUERIES_URL = os.environ.get("DB_BOOKS_QUERIES_URL", None)
    DB_BOOKS_QUERIES_PORT = os.environ.get("DB_BOOKS_QUERIES_PORT", None)
    DB_BOOKS_QUERIES_USER = os.environ.get("DB_BOOKS_QUERIES_USER", None)
    DB_BOOKS_QUERIES_PASS = os.environ.get("DB_BOOKS_QUERIES_PASS", None)
    DB_BOOKS_QUERIES_DATABASE = os.environ.get("DB_BOOKS_QUERIES_DATABASE", None)
    DB_BOOKS_QUERIES_COLLECTION = os.environ.get("DB_BOOKS_QUERIES_COLLECTION", None)
    should_raise_exception = False
    if DB_BOOKS_QUERIES_URL is None:
        print("[ERROR] DB_BOOKS_QUERIES_URL = None")
        should_raise_exception = True
    # In prod, a MongoDB cluster is used instead of a local instance of MongoDB.
    # MongoDB clusters don't accept port numbers.
    if DB_BOOKS_QUERIES_PORT is None and IS_DEV:
        print("[ERROR] DB_BOOKS_QUERIES_PORT = None")
        should_raise_exception = True
    if DB_BOOKS_QUERIES_USER is None:
        print("[ERROR] DB_BOOKS_QUERIES_USER = None")
        should_raise_exception = True
    if DB_BOOKS_QUERIES_PASS is None:
        print("[ERROR] DB_BOOKS_QUERIES_PASS = None")
        should_raise_exception = True
    if DB_BOOKS_QUERIES_DATABASE is None:
        print("[ERROR] DB_BOOKS_QUERIES_DATABASE = None")
        should_raise_exception = True
    if DB_BOOKS_QUERIES_COLLECTION is None:
        print("[ERROR] DB_BOOKS_QUERIES_COLLECTION = None")
        should_raise_exception = True
    if should_raise_exception:
        raise Exception(
            "[ERROR] Required credentials were not found in the environment variables"
        )

    # K8s includes something like DB_BOOKS_QUERIES_USER='...' to include the quotes themselves too.
    # Thus, sanitize it so that the env vars do not start with or end with quotes.
    DB_BOOKS_QUERIES_URL = sanitize_env_var(DB_BOOKS_QUERIES_URL)
    DB_BOOKS_QUERIES_PORT = (
        int(float(sanitize_env_var(DB_BOOKS_QUERIES_PORT))) if IS_DEV else None
    )
    DB_BOOKS_QUERIES_USER = sanitize_env_var(DB_BOOKS_QUERIES_USER)
    DB_BOOKS_QUERIES_PASS = sanitize_env_var(DB_BOOKS_QUERIES_PASS)
    DB_BOOKS_QUERIES_DATABASE = sanitize_env_var(DB_BOOKS_QUERIES_DATABASE)
    DB_BOOKS_QUERIES_COLLECTION = sanitize_env_var(DB_BOOKS_QUERIES_COLLECTION)

    CONFIGS = {
        IS_DEV: IS_DEV,
        DB_BOOKS_COMMANDS_URL: DB_BOOKS_COMMANDS_URL,
        DB_BOOKS_COMMANDS_PORT: DB_BOOKS_COMMANDS_PORT,
        DB_BOOKS_COMMANDS_USER: DB_BOOKS_COMMANDS_USER,
        DB_BOOKS_COMMANDS_PASS: DB_BOOKS_COMMANDS_PASS,
        DB_BOOKS_COMMANDS_DATABASE: DB_BOOKS_COMMANDS_DATABASE,
        DB_BOOKS_QUERIES_URL: DB_BOOKS_QUERIES_URL,
        DB_BOOKS_QUERIES_PORT: DB_BOOKS_QUERIES_PORT,
        DB_BOOKS_QUERIES_USER: DB_BOOKS_QUERIES_USER,
        DB_BOOKS_QUERIES_PASS: DB_BOOKS_QUERIES_PASS,
        DB_BOOKS_QUERIES_DATABASE: DB_BOOKS_QUERIES_DATABASE,
        DB_BOOKS_QUERIES_COLLECTION: DB_BOOKS_QUERIES_COLLECTION,
    }
    return CONFIGS
