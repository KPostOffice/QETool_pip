import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qeGraphMaker",
    version="0.0.2",
    author="Kevin Postlethwait",
    author_email="kpostlet@redhat.com",
    description="Create PDF Graphs from Google Sheets Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KPostOffice/QETool_pip",
    packages=setuptools.find_packages("pythonFiles"),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points = {
        'console_scripts': [
            'fileMaker=graphMaker.pythonFiles.createFile:main'
        ]
    },
)
