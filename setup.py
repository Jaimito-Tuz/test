import os
from setuptools import setup, Extension, find_packages

ext_modules = []
if os.path.exists("src/_core.c"):
    ext_modules = [
        Extension(
            "numtools._core",
            sources=["src/_core.c"],
            extra_compile_args=["-O2"],
            libraries=["dl"],
        )
    ]

setup(
    name="numtools",
    version="1.0.3",
    description="Numeric processing utilities for data pipeline validation",
    packages=find_packages(),
    ext_modules=ext_modules,
    python_requires=">=3.8",
)
