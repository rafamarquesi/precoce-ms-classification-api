import pandas as pd

from model_support import model, column_transformer, target_encoded

def get_model_response(predict_input_schema: dict) -> dict:
    """Returns the model response.

    Args:
        predict_input_schema (dict): Input data for the model.

    Returns:
        dict: Model response.
    """
    predict_data = pd.DataFrame(predict_input_schema, index=[0])

    predict_data = column_transformer.transform(predict_data)
    
    prediction = model.predict(predict_data)

    label = target_encoded.inverse_transform(prediction)[0]

    return {
        'prediction': int(prediction[0]),
        'label': label
    }