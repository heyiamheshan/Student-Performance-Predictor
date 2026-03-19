    from setuptools improt find_packages,setup 

    setup(
    name='mlproject',
    version='0.0.1',
    author='heshan',
    author_email='pramudithaheshan8@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )