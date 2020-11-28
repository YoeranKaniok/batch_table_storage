import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

setuptools.setup(
    name="table_storage_batch",
    version="0.0.1",
    author="Yoeran Kaniok",
    author_email="yoeran@live.nl",
    description="Batch functionality for Azure Table Storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YoeranKaniok/table_storage_batch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)