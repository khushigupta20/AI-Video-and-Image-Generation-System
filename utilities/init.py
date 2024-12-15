import utilities.config as config
import secrets

def startup(config_filename: str):
    config.load_config(config_filename)

    # Generate a random secret key of 32 bytes (256 bits)
    secret_key = secrets.token_hex(32)
    #config.JWT_SECRET_KEY = secret_key
