from setuptools import setup, find_packages

setup(
    name="busy-beaver",
    version="0.1.0",
    description="A Turing Machine simulator to explore Busy Beaver machines.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Matt Starolis",
    author_email="matt@starol.is",
    url="https://github.com/starolis/busy-beaver",
    packages=find_packages(),
    install_requires=[
        # Core Dependencies
<<<<<<< HEAD
=======
        "multiprocessing",
>>>>>>> 2bb4408107392638321447b0fbca6f59d9bf278b
        "functools",
        # Development Dependencies
        "flake8==6.0.0",
        "black==23.1.0",
        "pre-commit==2.20.0",
        "pytest==7.2.0",
    ],
    entry_points={
        "console_scripts": [
            "run-simulation=busy_beaver.simulation:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    keywords="turing machine busy beaver simulator",
    project_urls={
        "Source": "https://github.com/starolis/busy-beaver",
    },
)
