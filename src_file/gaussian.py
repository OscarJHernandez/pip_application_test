import numpy as np


class Gaussian:
    """
    The test class for the pip package
    """

    def __init__(self,x):
        self.x = x

    def fit_gaussian(self):
        
        x_mean = self.x.mean()
        x_std = self.x.std()

        return x_mean, x_std
