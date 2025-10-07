# hubconf.py - minimal YOLOv5 Hub config for local load
import torch
from pathlib import Path
from models.yolo import Model

dependencies = ['torch', 'yaml', 'numpy']

def custom(path='models/best_windows.pt', autoshape=True):
    """
    Load a custom YOLOv5 model for inference.
    """
    model = torch.load(path, map_location='cpu')
    if isinstance(model, dict) and 'model' in model:
        model = model['model']  # for state_dict format
    model.eval()
    return model
