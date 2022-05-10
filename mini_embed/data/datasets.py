import torch
from omegaconf import DictConfig


class ToxicDataset(torch.utils.data.Dataset):

    def __init__(self, cfg: DictConfig):
        pass
    
    def __len__(self):
        return 0
    
    def __getitem__(self):
        return None


class TextDataModule:

    def __init__(self, cfg: DictConfig):
        pass

    def setup(self):
        pass

    def train_data_loader(self):
        pass

    def test_data_loader(self):
        pass

    def valid_data_loader(self):
        pass