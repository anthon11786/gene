from setuptools import setup

setup(
    name='chat',
    version='0.1.0',
    py_modules=['main'],
    install_requires=[
        'Click',
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'gene = main:cli',
        ],
    },
)