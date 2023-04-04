import pandas as pd

from model_support import model, column_transformer, target_encoded

def get_model_response(predict_input_schema: dict) -> dict:
    """Returns the model response.

    Args:
        predict_input_schema (dict): Input data for the model.

    Returns:
        dict: Model response.
    """
    predict_data = pd.DataFrame(predict_input_schema)

    predict_data = column_transformer.transform(predict_data)
    
    prediction = model.predict(predict_data)

    label = target_encoded.inverse_transform(prediction)
    
    # TODO: Add the probability of the prediction, classification confidence (verify if the model has predict_proba).
    prediction_proba = model.predict_proba(predict_data)
    classes = target_encoded.inverse_transform(model.classes_)
    
    if predict_data.shape[0] != 1:
        
        predictions = []
        for i in range(predict_data.shape[0]):
            classes_probabilites = []
            for j in range(len(classes)):
                classes_probabilites.append({classes[j]: float(prediction_proba[i][j]) })

            predictions.append({
                'prediction': int(prediction[i]),
                'label': label[i],
                'class_probabilities': classes_probabilites
            })
        
        response = {'batch': predictions}
    else:
        classes_probabilites = []
        for i in range(len(classes)):
            classes_probabilites.append({classes[i]: float(prediction_proba[0][i]) })
        response = {
            'prediction': int(prediction[0]),
            'label': label[0],
            'class_probabilities': classes_probabilites
        }
    
    return response