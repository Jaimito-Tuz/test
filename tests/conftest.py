import pytest


@pytest.fixture
def sample_data():
    return [1.0, 2.0, 3.0, 4.0, 5.0]


@pytest.fixture
def large_sample():
    import random
    random.seed(42)
    return [random.uniform(0, 100) for _ in range(1000)]
