from syft._numpy.tensor.abstract import AbstractTensor
import numpy as np
import pytest


@pytest.mark.parametrize("method_name", ["__matmul__", "__add__"])
def test_subclass_method_type_and_values(method_name):
    x_ = np.array([[1, 2], [3, 4.]])
    target = x_.__getattribute__(method_name)(x_)

    x = AbstractTensor(x_)
    out = x.__getattribute__(method_name)(x)

    assert isinstance(target, np.ndarray)
    assert isinstance(out, AbstractTensor)
    assert (np.asarray(out) == target).all()