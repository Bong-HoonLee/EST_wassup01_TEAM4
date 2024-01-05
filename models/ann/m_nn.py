import torch.nn as nn

class MANN(nn.Module):
  def __init__(self, input_dim:int=10, output_dim:int=5, c_n:int=2, activation=nn.ReLU):
    super().__init__()
    self.lin1 = nn.Linear(input_dim*c_n, 512)
    self.lin2 = nn.Linear(512, output_dim)
    self.activation = activation
  def forward(self, x):
    x = x.flatten(1)    # (B, d_in * c_in)
    x = self.lin1(x)
    x = nn.BatchNorm1d(x)   # (B, d_hidden)
    x = self.activation(x)
    x = self.lin2(x)    # (B, d_out)
    return nn.Sigmoid(x)
    