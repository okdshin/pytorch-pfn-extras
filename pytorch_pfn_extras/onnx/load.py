import onnx
import json
import warnings
from pathlib import Path


def load_model(f, format=None, load_external_data=True):
    """Load model from ONNX file.

    Args:
        f: A file-like object or a string file path to be written to this
            file.
        format: A reserved arg
        load_external_data: If True and the external data under the same 
            directory of the model, load the external data
    """
    try:
        return onnx.load_model(f, format=format, load_external_data=load_external_data)
    except IOError as e:  # The ONNX may be stripped large tensor
        try:
            if json.loads(Path(e.filename).name)["type"] == "stripped":
                assert load_external_data
                warnings.warn(
                    'The specified ONNX is stripped large tensor. Set `load_external_data=False`.',
                    UserWarning)
                return onnx.load_model(f, format=format, load_external_data=False)
            else:
                raise e
        except:
            raise e