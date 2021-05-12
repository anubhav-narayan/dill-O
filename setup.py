from setuptools import setup, find_packages

with open('./README.md', 'r', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='dill-O',
    version='0.0.3',
    description='Small dill wrapper with Metadata',
    author='Anubhav Mattoo',
    author_email='anubhavmattoo@outlook.com',
    packages=find_packages(),
    install_requires=[
        'dill',
        'json',
        'jsonpickle'
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anubhav-narayan/dillO",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Development Status :: 3 - Alpha'
    ],
    python_requires=">=3.6"
)
