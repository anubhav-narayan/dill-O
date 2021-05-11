from setuptools import setup, find_packages

setup(
    name='dillo',
    version='0.0.1',
    description='Small dill wrapper with Metadata',
    author='Anubhav Mattoo',
    author_email='anubhavmattoo@outlook.com',
    packages=find_packages(),
    install_requires=[
        'dill',
        'json',
        'jsonpickle'
    ],
    license=open('./LICENSE', 'r').read(),
    long_description=open('./README.md', 'r').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Development Status :: 3 - Alpha'
    ]
)
