from setuptools import find_packages, setup
from typing import List

# Declare varaibel
HYPEN_DOT_E = '-e .'

def get_requirement_list(file_path:str) -> List[str]:
    '''
    Description: Return the list of libraries present
                 in requirements.txt file
    '''

    requirement_list = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirement_list = [req.replace('\n','') for req in requirements]

        if HYPEN_DOT_E in requirement_list:
            requirement_list.remove(HYPEN_DOT_E)

    return requirement_list

setup(
    name= 'Studnet Performance Machine Learning Project',
    version= '0.0.1',
    author= 'Umang Mudgal',
    author_email='mudgal0709@gmail.com',
    packages= find_packages(),
    install_requires=get_requirement_list('requirements.txt')
)