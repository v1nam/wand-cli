import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.readlines()

setuptools.setup(
    name="wand-cli",
    version="1.6",
    author="vinam",
    author_email="vinamraj01@gmail.com",
    description="A cli tool to compile over 26 languages instantly using the wandbox api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/v1nam/wandbox-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": ["wandbox=wandbox.cli_:main"],
    },
    keywords="wandbox cli compile run",
    install_requires=requirements,
    zip_safe=False,
)
