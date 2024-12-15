import argparse

import utilities.config
import utilities.init
import database.intialize

# Create ArgumentParser
parser = argparse.ArgumentParser()

# Define arguments
parser.add_argument("--config", type=str, help="Name of the config file to be used. By default it picks .env file.", default=".env")

# Parse arguments
args = parser.parse_args()

utilities.init.startup(args.config)
database.intialize.create_structure()
database.intialize.initialize_data()