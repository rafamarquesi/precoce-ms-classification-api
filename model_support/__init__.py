from flask import Flask

from model_support import utils

# Initialize the Flask application
app = Flask(__name__)

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