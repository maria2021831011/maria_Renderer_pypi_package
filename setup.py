import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.1"
REPO_NAME = "maria_Renderer_pypi_package"
AUTHOR_USER_NAME = "maria2021831011"
AUTHOR_EMAIL = "ritukhan534@gmail.com"
SRC_REPO = "mari2111render"

setuptools.setup(
    name=SRC_REPO,  # PyPI package name
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for rendering YouTube videos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},                 # tells setuptools to look in src/
    packages=setuptools.find_packages(where="src"),  # finds all packages under src/
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # ensure Python version compatibility
)
