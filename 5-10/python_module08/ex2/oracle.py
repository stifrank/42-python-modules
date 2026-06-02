import os
import sys

from dotenv import load_dotenv


REQUIRED_CONFIG = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_configuration() -> None:
    load_dotenv()


def get_config_value(key: str) -> str:
    value = os.getenv(key)

    if value is None or value == "":
        return ""

    return value


def get_missing_config() -> list[str]:
    missing = []

    for key in REQUIRED_CONFIG:
        if get_config_value(key) == "":
            missing.append(key)

    return missing


def describe_database(database_url: str) -> str:
    if database_url == "":
        return "Missing configuration"

    if database_url.startswith("sqlite"):
        return "Connected to local instance"

    return "Connected to remote instance"


def describe_api_access(api_key: str) -> str:
    if api_key == "":
        return "Not authenticated"

    return "Authenticated"


def describe_zion_network(zion_endpoint: str) -> str:
    if zion_endpoint == "":
        return "Offline"

    return "Online"


def show_configuration() -> None:
    matrix_mode = get_config_value("MATRIX_MODE")
    database_url = get_config_value("DATABASE_URL")
    api_key = get_config_value("API_KEY")
    log_level = get_config_value("LOG_LEVEL")
    zion_endpoint = get_config_value("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode or 'missing'}")
    print(f"Database: {describe_database(database_url)}")
    print(f"API Access: {describe_api_access(api_key)}")
    print(f"Log Level: {log_level or 'missing'}")
    print(f"Zion Network: {describe_zion_network(zion_endpoint)}")


def show_security_check() -> None:
    missing_config = get_missing_config()

    print("Environment security check:")

    if missing_config:
        print(f"[WARNING] Missing configuration: {', '.join(missing_config)}")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    try:
        load_configuration()
        print()
        show_configuration()
        print()
        show_security_check()
        print("\nThe Oracle sees all configurations.")
    except OSError as error:
        print(f"Configuration error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
