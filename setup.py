from setuptools import setup, find_packages

setup(
    name='pdfshrink',
    version='0.0.0',
    description='`pdfshrink` takes a number of PDF files and tries to optimize them through a suitable call to `ghostscript`.',
    long_description='Read the README',
    author='Federico Stra',
    author_email='stra.federico@gmail.com',
    # packages=find_packages(),
    py_modules=['pdfshrink'],
    install_requires=[],
    extras_require={
        'test': ['coverage']
    },
    entry_points={
        'console_scripts': [
            'pdfshrink=pdfshrink:main',
        ],
    },
)
