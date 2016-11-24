import numpy as np

def assertNpEquals(actual, expected):
    actual = np.array(actual)
    expected = np.array(expected)
    # print expected.shape

    assert actual.ndim == expected.ndim
    for i in range(actual.ndim):
        assert actual.shape[i] == expected.shape[i]

    # print expected - actual

    assert np.allclose(actual, expected, atol=1e-06)  # test if nearly same elements values