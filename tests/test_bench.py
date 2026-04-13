import pytest
from numtools import compute_hash, normalize_buffer, validate_checksum
from numtools.bench import run_benchmark, verify


def test_compute_hash_returns_int(sample_data):
    h = compute_hash(str(sample_data).encode())
    assert isinstance(h, int)


def test_normalize_buffer_mean_centers(sample_data):
    result = normalize_buffer(sample_data)
    assert abs(sum(result)) < 1e-9


def test_normalize_buffer_length(sample_data):
    result = normalize_buffer(sample_data)
    assert len(result) == len(sample_data)


def test_validate_checksum_match():
    data = b"pipeline-v1"
    h = compute_hash(data)
    assert validate_checksum(h, h) is True


def test_validate_checksum_mismatch():
    assert validate_checksum(12345, 99999) is False


def test_run_benchmark_structure(sample_data):
    result = run_benchmark(sample_data)
    assert "digest" in result
    assert "n" in result
    assert result["n"] == len(sample_data)


@pytest.mark.parametrize("size", [10, 100, 500])
def test_benchmark_scales(size):
    import random
    random.seed(size)
    data = [random.uniform(0, 1) for _ in range(size)]
    result = run_benchmark(data)
    assert result["n"] == size
