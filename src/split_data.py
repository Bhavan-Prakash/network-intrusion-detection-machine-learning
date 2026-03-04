from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split

train_strat,test_strat = train_test_split(
    data,
    test_size = 0.2,
    random_state = 42,
    stratify = data["Label"]
)

train_main = train_strat