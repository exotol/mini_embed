import hydra
from hydra.utils import instantiate
from omegaconf import (
    DictConfig,
    OmegaConf
)
from mini_embed import (
    CBOW,
    TextDataModule,
    CustomTrainer
)


@hydra.main(config_name="start", config_path=None)
def run_train(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    data_module = TextDataModule(cfg)

    model = instantiate(cfg.model)

    trainer = CustomTrainer(cfg)

    trainer.fit(model, data_module)


if __name__ == "__main__":
    run_train()