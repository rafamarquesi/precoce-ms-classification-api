from pathlib import Path
from joblib import load

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

    Args:
        file_path (str): Path of the file will be loaded.
    Returns:
        object: File loaded.
    """

    return load(file_path)