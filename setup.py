from setuptools import setup, find_packages

setup(
    name="timeseries_app",
    version="0.1",
    packages=find_packages(where="."), 
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "scipy",
        "statsmodels"
    ],
)