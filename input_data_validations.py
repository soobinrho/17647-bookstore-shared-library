import re
import jwt
import datetime


def check_is_valid_JWT(input_JWT: str) -> bool:
    # Structure of JWT:
    # HEADER_BASE64URL_ENCODED.PAYLOAD_BASE64URL_ENCODED.SIGNATURE
    # In this assignment, signature can be any value. Note that
    # signature's purpose is to verify that the header and the payload
    # originate from where it claims to be. The header and payload are
    # still base64 decodable without any key.
    if input_JWT.count(".") != 3:
        return False

    list_JWT_three_parts = input_JWT.split(".")
    for part in list_JWT_three_parts:
        if len(part) < 1:
            return False

    JWT_payload = jwt.decode(input_JWT, options={"verify_signature": False})

    # We don't need the header for this assignment, but adding this
    # for my future reference:
    _ = jwt.get_unverified_header(input_JWT)

    if "sub" not in JWT_payload or "exp" not in JWT_payload or "iss" not in JWT_payload:
        return False

    JWT_payload_sub = str(JWT_payload["sub"])
    LIST_VALID_SUBS = ["starlord", "gamora", "drax", "rocket", "groot"]
    if JWT_payload_sub.lower() not in LIST_VALID_SUBS:
        return False

    JWT_payload_exp = str(JWT_payload["exp"])
    if not check_is_valid_unix_epoch(JWT_payload_exp):
        return False
    else:
        input_time = datetime.datetime.fromtimestamp(JWT_payload_exp)
        now_time = datetime.datetime.now()
        if input_time <= now_time:
            return False

    JWT_payload_iss = str(JWT_payload["iss"])
    if JWT_payload_iss != "cmu.edu":
        return False

    return True


def check_is_valid_unix_epoch(input_time: str) -> bool:
    try:
        datetime.datetime.fromtimestamp(input_time)
        return True
    except Exception:
        return False


def check_is_valid_price(price) -> bool:
    price = str(price)
    if len(str(price)) == 0:
        return False

    try:
        if float(price) < 0:
            return False
    except ValueError:
        return False
    else:
        # Price can have 0 to 2 decimal places.
        if "." in price:
            decimal_points = len(price.split(".")[1])
            if decimal_points >= 3:
                return False

    return True


def check_is_valid_quantity(quantity) -> bool:
    quantity = str(quantity)
    if len(str(quantity)) == 0:
        return False

    try:
        _ = float(quantity)
    except ValueError:
        return False

    return True


def check_is_valid_email(userId) -> bool:
    userId = str(userId)
    if len(userId) == 0:
        return False

    # Source: https://stackoverflow.com/a/8022584
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", userId):
        return False

    return True


def check_is_valid_state_abbr(state: str) -> bool:
    if len(state) != 2:
        return False

    # Source: https://stackoverflow.com/a/65714104
    list_states = [
        "AL",
        "AK",
        "AS",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "DC",
        "FL",
        "GA",
        "GU",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "MP",
        "OH",
        "OK",
        "OR",
        "PA",
        "PR",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VI",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
    ]
    if state not in list_states:
        return False

    return True
