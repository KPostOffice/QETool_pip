import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qe_cmd_line_tool",
    version="0.0.1",
    author="Kevin Postlethwait",
    author_email="kpostlet@redhat.com",
    description="Create PDF Graphs from Google Sheets Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KPostOffice/QETool_pip",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
