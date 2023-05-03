import os

from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_matomo import *

from model_support import utils

# Initialize Sentry
sentry_sdk.init(
    dsn=os.environ['FLASK_API_SENTRY_DSN'],
    release=os.environ['FLASK_API_VERSION'].split('-')[0],
    environment=os.environ['FLASK_API_STAGE'],
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

# Initialize the Flask application
app = Flask(__name__)

# Initialize Matomo
# TODO: verificar com camilo, está dando erro flask_matomo.MatomoError: Status code: 400 ao tentar acessar a URL https://hit.embrapa.io/piwik.php, somente domínios específicos que podem acessar?
matomo = Matomo(
    app=app,
    matomo_url='https://hit.embrapa.io',
    id_site=int(os.environ['FLASK_API_MATOMO_ID']),
    token_auth=os.environ['FLASK_API_MATOMO_TOKEN'] # TODO: verificar com camilo, The token_auth parameter can be found in the area API in the settings of Matomo. It is required for tracking the ip address
)

# Load the model
model = utils.load_object(
    file_path=utils.get_file_path(folder_path='./serialized_files/model/')
)

# Load the column transformer
column_transformer = utils.load_object(
    file_path=utils.get_file_path(folder_path='./serialized_files/column_transformer/')
)

# Load the target encoder
target_encoded = utils.load_object(
    file_path=utils.get_file_path(folder_path='./serialized_files/target_encoded/')
)