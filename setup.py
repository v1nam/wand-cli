import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
        'requests==2.25.1',
        'Pygments==2.7.4',
        'prompt-toolkit==3.0.11',
        'rich==9.8.2',
        'argparse'
        ]

setuptools.setup(
    name="wand-cli",
    version="2.4.8",
    author="vinam",
    author_email="vinamraj01@gmail.com",
    description="A cli tool with an in-place terminal editor to compile over 27 languages instantly using the wandbox api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/v1nam/wand-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    scripts=["wand"],
    keywords="wandbox cli compile run compiler",
    install_requires=requirements,
    zip_safe=False,
)
