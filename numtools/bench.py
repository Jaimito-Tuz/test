from . import compute_hash, normalize_buffer, validate_checksum


def run_benchmark(samples):
    """Run a standard validation pass over a list of float samples."""
    normalized = normalize_buffer(samples)
    digest = compute_hash(str(normalized).encode())
    return {"digest": digest, "n": len(normalized), "mean_centered": normalized}


def verify(samples, expected_digest):
    """Verify that a sample set matches an expected digest."""
    result = run_benchmark(samples)
    return validate_checksum(result["digest"], expected_digest)
