from setuptools import setup
from typing import List


#Declaring variable for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Amar"
DESCRIPTION="This is the first FSDS nov batch ML project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: this function is going to return list of requirement
    mentioned in requirements.txt file
    
    return this function is going to return a list which contain name of
    libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)



