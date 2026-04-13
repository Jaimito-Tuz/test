# numtools

Numeric processing utilities for data pipeline validation. Provides fast hashing,
normalization, and checksum verification backed by a compiled C extension.

## Install

```bash
pip install -e .
```

## Usage

```python
from numtools import compute_hash, normalize_buffer, validate_checksum
from numtools.bench import run_benchmark

result = run_benchmark([1.0, 2.5, 3.7, 4.2])
print(result)
```

## Run tests

```bash
pytest tests/
```
