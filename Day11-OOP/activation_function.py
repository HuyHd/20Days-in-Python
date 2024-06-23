import torch
import torch.nn as nn


class ReLUActivateFunction(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.relu(x)


class SigmoidActivateFunction(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.sigmoid(x)


# Testcases:
input_tensor = torch.tensor([1, -5, 1.5, 2.7, -5])
output_relu = ReLUActivateFunction().forward(input_tensor)
output_sigmoid = SigmoidActivateFunction().forward(input_tensor)
print(f"- ReLU: {output_relu}\n- Sigmoid: {output_sigmoid}")
