"""
hubconf.py - Minimal Torch Hub interface for local YOLOv5 inference.
"""

import torch
from pathlib import Path

dependencies = ['torch']

def custom(path='models/best_windows.pt', autoshape=True):
    """
    Load a custom YOLOv5 model for inference.
    """
    model_path = Path(path)
    model = torch.load(model_path, map_location='cpu')  # load model
    if isinstance(model, dict) and 'model' in model:
        model = model['model']  # handle state_dict format
    model.eval()
    return model
