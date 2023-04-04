from flask import request, jsonify

from marshmallow import ValidationError

from model_support import app
from model_support.functions import get_model_response
from model_support.predict_input_schema import PredictInputSchema

predict_input_schema = PredictInputSchema()

model_name = 'Precoce MS'
version = 'v1.0.0'

@app.route('/info', methods=['GET'])
def info():
    """Return model information, version, how to call"""
    result = {}

    result['name'] = model_name
    result['version'] = version

    return result

@app.route('/health', methods=['GET'])
def health():
    """Return service health"""
    return 'ok'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        inputs = [predict_input_schema.load(request.get_json())]
    except ValidationError as err:
        return err.messages, 400
    
    try:
        response = get_model_response(predict_input_schema=inputs)
    except ValueError as e:
        return {'error': str(e).split('\n')[-1].strip()}, 500

    return jsonify(response)

@app.route('/predict_batch', methods=['POST'])
def predict_batch():
    try:
        inputs = []
        for item in request.get_json()['batch']:
            inputs.append(predict_input_schema.load(item))
    except ValidationError as err:
        return err.messages, 400
    
    try:
        response = get_model_response(predict_input_schema=inputs)
    except ValueError as e:
        return {'error': str(e).split('\n')[-1].strip()}, 500

    return jsonify(response)
