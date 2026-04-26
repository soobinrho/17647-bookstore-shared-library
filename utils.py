import time


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
