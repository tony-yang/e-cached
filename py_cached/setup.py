from setuptools import setup, find_packages

setup(
    name='pycached',
    version='0.1',
    packages=find_packages(),

    entry_points = {
        'console_scripts': [
            'pycache=py_cached.cli.ecache:main',
            'pycached=py_cached.cli.ecached:main'
        ]
    },

    install_requires=[
        'coverage'
    ]
)
