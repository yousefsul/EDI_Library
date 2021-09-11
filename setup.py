# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding


setup(
    name="Edi_Library",
    version="0.1.0",
    description="EDI library",
    author="Yousef Suliman",
    author_email="",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["Edi_Library"],
    include_package_data=True,
    install_requires=["shortuuid"]
)