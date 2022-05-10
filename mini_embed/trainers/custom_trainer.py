from omegaconf import DictConfig
from torch import nn
from mini_embed import TextDataModule


class CustomTrainer:

    def __init__(self, cfg: DictConfig):
        pass

    def fit(self, model: nn.Module, data_module: TextDataModule):
        pass
