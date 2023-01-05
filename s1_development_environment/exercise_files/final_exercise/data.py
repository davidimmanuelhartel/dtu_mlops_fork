import torch
import numpy as np

def mnist():
    # exchange with the corrupted mnist dataset
    train_ims = torch.tensor(np.array([np.load(f"data/corruptmnist_v2/train_{i}.npz")["images"] for i in range(5,8)]).reshape(-1,28,28))
    train_labels = torch.tensor(np.array([np.load(f"data/corruptmnist_v2/train_{i}.npz")["labels"] for i in range(5,8)]).reshape(-1))
    test_ims = torch.tensor(np.load(f"data/corruptmnist/test.npz")["images"])
    test_labels = torch.tensor(np.load(f"data/corruptmnist/test.npz")["labels"])
    return list(zip(train_ims, train_labels)),list(zip(test_ims, test_labels))

