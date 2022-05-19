import os
from base64 import b64decode

import boto3
import yaml

# Local flag to know if local config.yaml was loaded
__read_local = False
CONFIG = {}

# Load and read local config
try:
    LOCAL = os.path.dirname(os.path.dirname(__file__))
    CONFIG_FILE = open(os.path.join(LOCAL, 'config.yaml'))
    CONFIG = yaml.load(CONFIG_FILE, Loader=yaml.FullLoader)
    __read_local = True
except Exception as e:
    __read_local = False
    print(e)

# Load and read amazon kms enviornment variables if the local config wasn't loaded
if not __read_local:
    try:
        REACT_BASE_URL = os.environ['REACT_BASE_URL']

        MONGO_PASSWORD = boto3.client('kms').decrypt(
            CiphertextBlob=b64decode(os.environ['MONGO_PASSWORD']),
            EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
        )['Plaintext'].decode('utf-8')

        MONDO_USER = boto3.client('kms').decrypt(
            CiphertextBlob=b64decode(os.environ['MONGO_USER']),
            EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
        )['Plaintext'].decode('utf-8')

        CONFIG = {
            "REACT_BASE_URL": REACT_BASE_URL,
            "MONGO_PASSWORD": MONGO_PASSWORD,
            "MONGO_USER": MONGO_USER
        }
    except Exception as e:
        print(e)
        raise Exception("Unable to load local or AWS enviornment variables")
