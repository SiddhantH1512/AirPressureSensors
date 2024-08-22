from setuptools import setup, find_packages
from typing import List

package = find_packages()

def get_requirements() -> List[str]:
    requirement_list: List[str] = []
    with open("requirements.txt", "r") as file:
        requirement_list = file.read().splitlines()
        requirement_list = [req for req in requirement_list if not req.startswith('-e')]
    return requirement_list


setup(
    author="Siddhant",
    version="0.0.1",
    author_email="siddhanthardikar6@gmail.com",
    packages=package,
    name="sensor",
    install_requires=get_requirements()
)