from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e.' ## it will automatically install setup.py file

def get_requirements(file_path:str)->list[str]:
    """
    This function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements 
        
    
  
setup(
    name='MLProject',
    version='0.1',
    author='Basant',
    author_email='basantb643@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)
