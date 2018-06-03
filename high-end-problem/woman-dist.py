import random
from scipy.stats import norm
for x in range(0, 50):
    print(norm.ppf(random.uniform(0, 1), loc=175.5, scale=7.4))
