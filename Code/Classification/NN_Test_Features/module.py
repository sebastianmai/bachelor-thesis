import numpy as np
import torch
from lightning.pytorch.loggers import TensorBoardLogger
from sklearn.model_selection import train_test_split
from torch import nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
import pytorch_lightning as pl
import torch.utils.data as data
import pandas as pd
from torchmetrics import Accuracy

path_to_data = "./RED/CYBRES_RED_CH1.csv"

class LitModule(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(nn.Linear(10, 128), nn.ReLU(), nn.Linear(128, 64), nn.ReLU(), nn.Linear(64, 3))
        self.accuracy = Accuracy(task='multiclass', num_classes=3)

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = F.cross_entropy(y_hat, y)
        self.log('train_loss', loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = F.cross_entropy(y_hat, y)
        self.log('val_loss', loss)

    def test_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = F.cross_entropy(y_hat, y)
        preds = torch.argmax(y_hat, dim=1)
        acc = self.accuracy(preds, y)
        self.log('test_loss', loss)
        self.log('test_accuracy', acc)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

class CustomDataset(data.Dataset):
    def __init__(self, csv_file, split, transform=None):
        self.data = pd.read_csv(csv_file)
        self.transform = transform

        train_data, test_data = train_test_split(self.data, test_size=0.2, random_state=42)
        train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42)


        if split == 'train':
            self.data = train_data
        elif split == 'val':
            self.data = val_data
        elif split == 'test':
            self.data = test_data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        features = self.data.iloc[idx, :-1].values.astype(np.float32)
        label = self.data.iloc[idx, -1]

        if self.transform:
            features = self.transform(features)

        return features, label

train_dataset = CustomDataset(csv_file=path_to_data, split='train', transform=None)
val_dataset = CustomDataset(csv_file=path_to_data, split='val', transform=None)
test_dataset = CustomDataset(csv_file=path_to_data, split='test', transform=None)

train_dataloader = DataLoader(train_dataset, batch_size=16, shuffle=True, num_workers=7)
val_dataloader = DataLoader(val_dataset, batch_size=16, num_workers=7)
test_dataloader = DataLoader(test_dataset, batch_size=16, num_workers=7)


model = LitModule()
trainer = pl.Trainer(
    max_epochs=10,
    logger=TensorBoardLogger('logs/', name='test_classifier'),
    log_every_n_steps=1,
)

trainer.fit(model, train_dataloader, val_dataloader)
trainer.test(model, dataloaders=test_dataloader)