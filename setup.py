from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="pdf_examiner",            
    version="1.0.0",
    author="5f0",
    url="https://github.com/5f0ne/pdf-examiner",
    description="Provides an overview of the inner file structure of a PDF and extracts /URI and /JS data.",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    package_data={
        "pdf_examiner.data": ["options.json"]
    },
    install_requires=[
        "hash_calc"
    ],
    entry_points={
        "console_scripts": [
            "pdf_examiner = pdf_examiner.__main__:main"
        ]
    }
)