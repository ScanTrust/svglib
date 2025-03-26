import sys
from pathlib import Path

from setuptools import setup, find_packages

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(
    packages=find_packages(),
    install_requires=Path("requirements.txt").read_text().splitlines(),
    setup_requires=pytest_runner
)
