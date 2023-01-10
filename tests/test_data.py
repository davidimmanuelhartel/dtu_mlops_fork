# importing sys
import sys
sys.path.insert(0, '/Users/davidhartel/Desktop/dtu_mlops_fork/s1_development_environment/exercise_files/final_exercise')
# import data
from data import mnist 

train_set, test_set = mnist()
N_train = 15000
N_test = 5000


# assert that the length of the train and test set is correct
assert len(train_set) == N_train or len(test_set) == N_test

# assert that each datapoint has shape [28,28] or [728] depending on how you choose to format
for image, label in train_set:
    assert image.shape == (28, 28) or image.shape == (728,)
    assert label in range(10)

# assert that all labels are represented
data_set_labels = set([int(label) for image, label in train_set])
all_labels = set(range(10))
assert data_set_labels == all_labels