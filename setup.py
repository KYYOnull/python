
from setuptools import setup, find_packages

setup(
    name="kyyoGPUtool",
    version="0.0.1",
    description="my gpu tools 类似 nvidia-smi",
    author="kyyo",
    packages=find_packages(),
    install_requires=["prettytable", "nvidia-ml-py"],
    license="LICENSE",
    entry_points={
        "console_scripts": [
            "gpu-tools = kyyoGPUtool.main:monitor_script"
        ]
    }
)
