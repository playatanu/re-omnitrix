import os

import torch
import torchvision

from helper import resource_path

MODEL_PATH = 'assets/model/ben10.pt'

transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize((224, 224)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

classes = ['Dimondhead',
 'FourArms',
 'Ghostfreak',
 'GreyMatter',
 'Heatblast',
 'Ripjaws',
 'Stinkfly',
 'Upgrade',
 'Wildmutt',
 'XLR8']

model = torch.jit.load(resource_path(MODEL_PATH))
model.eval()

def predict(image):
    image_tensor = transform(image)
    with torch.no_grad():
        outputs = model(image_tensor.unsqueeze(0))
        _, predicted = torch.max(outputs, 1)
        return classes[predicted.item()]
    