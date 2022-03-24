import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amason13",
    version="0.0.1",
    author="Ashley Mason",
    author_email="ashmason1389@gmail.com",
    description="PlusEvAnalytics course python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amason13/plusev",
    project_urls={
        "Bug Tracker": "https://github.com/amason13/plusev/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
