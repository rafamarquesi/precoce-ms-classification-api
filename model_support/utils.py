from pathlib import Path
from joblib import load

from xgboost import XGBClassifier
from pytorch_tabnet.tab_model import TabNetClassifier

_ESTIMATORS_WITH_SAVE_LOAD_METHOD = [
    XGBClassifier().__class__.__name__,
    TabNetClassifier(device_name='cpu').__class__.__name__
]

def get_file_path(folder_path: str) -> str:
    """
    Get the path for the file.

    Args:
        path (str): Folder path for the file.
    Returns:
        str: Path of the file.
    """
    file_path = str
    
    source_path = Path(folder_path)
    
    for child in source_path.iterdir():
        if child.is_file() and child.name != '.gitkeep':
            file_path = str(child)

    return file_path

def load_object(file_path: str) -> object:
    """
    Loads the objects saved during of grid search, for example, the best estimator.
    Wtih the file is not in the list of estimators with save and load methods, the load method from joblib is used.

    Args:
        file_path (str): Path of the file will be loaded.
    Returns:
        object: File loaded.
    """

    object_ = object
    object_name = str

    for estimator in _ESTIMATORS_WITH_SAVE_LOAD_METHOD:
        initial_index = file_path.find(estimator)
        if initial_index != -1:
            final_index = initial_index + len(estimator)
            object_name = file_path[initial_index:final_index]
            break

    if object_name not in _ESTIMATORS_WITH_SAVE_LOAD_METHOD:
        object_ = load(file_path)
    else:
        # If XGBoost
        if object_name == _ESTIMATORS_WITH_SAVE_LOAD_METHOD[0]:
            object_ = XGBClassifier()
            object_.load_model(file_path)
        # If TabNetClassifier
        elif object_name == _ESTIMATORS_WITH_SAVE_LOAD_METHOD[1]:
            object_ = TabNetClassifier(device_name='cpu')
            object_.load_model(file_path)
        else:
            raise ValueError(
                'File not found. Please, check the path ({}).'.format(file_path))

    return object_