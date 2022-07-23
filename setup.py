#!/usr/bin/env python

# This file is inspired by https://github.com/PyTorchLightning/metrics/blob/master/setup.py.

import os
from importlib.util import module_from_spec, spec_from_file_location

from setuptools import find_packages, setup

_PATH_ROOT = os.path.realpath(os.path.dirname(__file__))
_README_FILE_NAME = "README.md"


def _load_py_module(fname, pkg="torch_emd"):
    spec = spec_from_file_location(os.path.join(pkg, fname), os.path.join(_PATH_ROOT, pkg, fname))
    py = module_from_spec(spec)
    spec.loader.exec_module(py)
    return py


setup_tools = _load_py_module("setup_tools.py")
about = _load_py_module("__about__.py")


BASE_REQUIREMENTS = setup_tools._load_requirements(path_dir=_PATH_ROOT, file_name="requirements.txt")
# Test requirements
_test_reqs = setup_tools._load_requirements(path_dir=_PATH_ROOT, file_name="requirements/test.txt")
TEST_REQUIREMENTS = BASE_REQUIREMENTS + _test_reqs
_docs_reqs = setup_tools._load_requirements(path_dir=_PATH_ROOT, file_name="requirements/docs.txt")
_devel_reqs = setup_tools._load_requirements(path_dir=_PATH_ROOT, file_name="requirements/devel.txt")
DEVEL_REQUIREMENTS = TEST_REQUIREMENTS + _docs_reqs + _devel_reqs

with open(os.path.join(_PATH_ROOT, _README_FILE_NAME), encoding="utf-8") as f:
    README_FILE = f.read()


setup(
    name="torch_emd",
    version=about.__version__,
    url=about.__homepage__,
    author=about.__author__,
    author_email=about.__author_email__,
    short_description=about.__description__,
    long_description=README_FILE,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests", "tests.*", "docs"]),
    keywords=["statistics", "machine learning"],
    python_requires=">=3.8",
    install_requires=BASE_REQUIREMENTS,
    extras_require={"test": TEST_REQUIREMENTS, "dev": DEVEL_REQUIREMENTS},
    include_package_data=True,
    classifiers=[
        "Natural Language :: English",
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
