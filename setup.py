from setuptools import find_packages,setup
from typing import List,Dict

def get_requirements() -> List[str]:
    requirement_list : List[str] =[]
    return requirement_list


setup(
    name = "sensor",
    version = "0.0.1",
    author = "Atanu Chowdhury",
    author_email="atanuc73@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)