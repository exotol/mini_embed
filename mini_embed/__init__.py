__version__ = '0.1.0'


from .modules.cbow import CBOW
from .data.datasets import TextDataModule
from .trainers.custom_trainer import CustomTrainer