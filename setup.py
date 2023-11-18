import setuptools

__version__ = "0.0.0"
REPO_NAME = "itest"
AUTHOR_USER_NAME = "Musician9DX"
SRC_REPO = "itest"
AUTHOR_EMAIL = "vamsir863@gmail.com"

setuptools.setup(
    name="itest",
    version=__version__,
    author="Musician9DX",
    author_email="vamsir863@gmail.com",
    description="nops performed",
    url="https://github.com/Musician9dx/itest",
    project_urls={
        "Bug Tracker": "https://github.com/Musician9dx/itest" + "/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
