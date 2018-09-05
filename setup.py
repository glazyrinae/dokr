import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dokr',
    version='0.2',
    scripts=['dokr'] ,
    author="Deepak Kumar",
    author_email="deepak.kumar.iet@gmail.com",
    description="A Docker and AWS utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/javatechy/dokr",
    packages=setuptools.find_packages(),
    py_modules = ['ecs_helper', 'docker_helper'],
    install_requires=[
        'ecs-deploy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )