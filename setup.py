    from setuptools improt find_packages,setup 

    def get_requiremnts(file_path)->List[str]:
        '''
        This function will return the list of requirements 
        '''
        requirements=[]
        with open(file)as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]

    setup(
    name='mlproject',
    version='0.0.1',
    author='heshan',
    author_email='pramudithaheshan8@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )