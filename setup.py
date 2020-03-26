import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Number-guessing-game",
    version="0.0.1",
    author="Eric Gafner",
    author_email="pgoonghang@yahoo.com",
    description="Simple Japanese language number guessing game for OS X",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pgoonghang/Number-guessing-game",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
