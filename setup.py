import setuptools

with open("tuyapower/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tuyapower",
    version="0.0.20",
    author="Jason Cox",
    author_email="jason@jasonacox.com",
    description="Pull power and state data from Tuya WiFi smart devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jasonacox/tuyapower",
    packages=setuptools.find_packages(),
    install_requires=[
        'pytuya',
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
