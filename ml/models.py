import os

import torch
from torch import nn
from torchvision.models import resnet18

from mldemo.settings import BASE_DIR

DEFAULT_MODEL_PATH = os.path.join(BASE_DIR, "model.pt")


def cat_dog_classifier(pretrained=True):
    model = resnet18(pretrained=pretrained)
    model.fc = nn.Linear(512 * 1, 2)
    return model


def load_default_model(path=DEFAULT_MODEL_PATH):
    model = cat_dog_classifier()
    model.load_state_dict(torch.load(path, map_location="cpu"))
    model.eval()
    return model
