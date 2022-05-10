import torch
from torch import nn
from omegaconf import DictConfig


class CBOW(nn.Module):

    def __init__(self, config: DictConfig):
        pass
        # self.look_up_table = nn.Embedding(
        #
        # )
        # self.hidden = nn.Linear(
        #
        # )
        # self.out = nn.Linear(
        #
        # )

    def forward(self, data: torch.Tensor):
        # data = self.look_up_table(data)
        # data = self.hidden(data)
        # data = self.out(data)
        return data