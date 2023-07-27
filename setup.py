from setuptools import setup
from pkg_resources import parse_requirements

# Read the requirements.txt file and parse the requirements
with open('requirements.txt') as f:
    requirements = [str(req) for req in parse_requirements(f)]

setup(
    name="git_example",
    version="0.1.0",
    description="Description of your project",
    author="Your Name",
    author_email="your@email.com",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
