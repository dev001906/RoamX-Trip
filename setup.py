from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This will return list of requrements
    """
    requirement_list:List[str] = []

    try:
        #Open and Read requirements.txt
        with open('requirements.txt', 'r') as file:
            #Read the lines
            lines = file.readlines()
            #Process each line
            for line in lines:
                #Strip whitespace and newline chars
                requirement = line.strip()
                #Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_list

print(get_requirements())
setup(
    name="ROAMX-TRIP",
    version="0.0.1",
    author="Dev",
    author_email="devendra.sadinsar@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)