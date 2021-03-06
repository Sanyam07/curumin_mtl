from sklearn.linear_model import Lasso

from paje.searchspace.hp import RealHP
from paje.searchspace.configspace import ConfigSpace
from numpy.random import uniform
from paje.ml.element.modelling.supervised.regressor.regressor import Regressor


class LASSO(Regressor):
    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)
        self.model = Lasso(**self.param())

    @classmethod
    def cs_impl(cls):
        hps = {'alpha': RealHP(uniform,low=1e-5,high=10.0)}

        return ConfigSpace(name='LASSO', hps=hps)
