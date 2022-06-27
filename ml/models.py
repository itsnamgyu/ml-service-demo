import os

import torch

from mldemo.settings import BASE_DIR

DEFAULT_MODEL_PATH = os.path.join(BASE_DIR, "model.pt")


class CatDogClassifier(torch.nn.Module):
    def __init__(self):
        pass

    def forward(self, x):
        return torch.tensor([1, 0], device=x.device)


def load_default_model(path=DEFAULT_MODEL_PATH):
    model = CatDogClassifier()
    model.load_state_dict(torch.load(path))
    return model


def save_default_model(model, path=DEFAULT_MODEL_PATH):
    torch.save(model.state_dict(), path)
