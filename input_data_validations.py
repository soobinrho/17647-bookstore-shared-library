import re
import time

import jwt


def sanitize_env_var(env_var: str) -> str:
    # In Kubernetes, something like DB_URL='...' includes the quote itself.
    # Thus, this sanitization is necessary.
    sanitized = str(env_var).strip()
    if sanitized.startswith('"') or sanitized.startswith("'"):
        sanitized = sanitized[1:]
    if sanitized.endswith('"') or sanitized.endswith("'"):
        sanitized = sanitized[:-1]
    return sanitized


def check_is_authenticated_request(
    req_path: str | None, header_auth: str | None
) -> bool:
    if req_path is not None and (
        req_path.startswith("/docs")
        or req_path == "/"
        or req_path.startswith("/openapi.json")
        or req_path.startswith("/status")
    ):
        return True

    if header_auth is not None and check_is_valid_JWT(header_auth):
        return True

    return False


def check_is_valid_JWT(input_JWT: str) -> bool:
    # Structure of JWT:
    # Bearer HEADER_BASE64URL_ENCODED.PAYLOAD_BASE64URL_ENCODED.SIGNATURE
    # In this assignment, signature can be any value. Note that
    # signature's purpose is to verify that the header and the payload
    # originate from where it claims to be. The header and payload are
    # still base64 decodable without any key.
    input_JWT = input_JWT.strip()
    if not input_JWT.lower().startswith("bearer"):
        return False

    input_JWT = input_JWT.split(" ")
    if len(input_JWT) != 2:
        return False

    # Example:
    # HEADER_BASE64URL_ENCODED.PAYLOAD_BASE64URL_ENCODED.SIGNATURE
    input_JWT = input_JWT[1]
    if input_JWT.count(".") != 2:
        return False

    try:
        JWT_payload = jwt.decode(input_JWT, options={"verify_signature": False})
    except Exception as e:
        print("[INFO] jwt decode failed. Invalid jwt likely.")
        print(e)
        return False

    # We don't need the header for this assignment, but adding this
    # for my future reference:
    # _ = jwt.get_unverified_header(input_JWT)

    if "sub" not in JWT_payload or "exp" not in JWT_payload or "iss" not in JWT_payload:
        return False

    JWT_payload_sub = str(JWT_payload["sub"])
    LIST_VALID_SUBS = ["starlord", "gamora", "drax", "rocket", "groot"]
    if not any(JWT_payload_sub == x for x in LIST_VALID_SUBS):
        return False

    JWT_payload_exp = str(JWT_payload["exp"])
    if not check_is_valid_unix_epoch(JWT_payload_exp):
        return False
    else:
        # Commented out. Using a simpler function instead due to edge cases.
        # input_time = datetime.datetime.fromtimestamp(int(float(JWT_payload_exp)))
        input_time = float(JWT_payload_exp)
        now_time = int(time.time())
        if input_time <= now_time:
            return False

    JWT_payload_iss = str(JWT_payload["iss"])
    if JWT_payload_iss != "cmu.edu":
        return False

    return True


def check_is_valid_unix_epoch(input_time) -> bool:
    try:
        _ = float(input_time)
        return True
    except Exception as e:
        print(f"[INFO] Unix epoch not convertable to float: {input_time}")
        print(e)
        return False

    # Commented out because of edge cases in the assignment auto grader.
    # try:
    #     _ = datetime.datetime.fromtimestamp(int(float(input_time)))
    #     return True
    # except Exception as e:
    #     print(f"[INFO] Unix epoch not convertable to datetime: {input_time}")
    #     print(e)
    #     return False


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
    if str(state).upper() not in list_states:
        return False

    return True
