from setuptools import setup, find_packages

setup(
    name='sprayer',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'urllib3'
    ],
    entry_points={
        'console_scripts': [
            'sprayer = sprayer.main:main'
        ]
    },
    url='https://github.com/cyberduck404/sprayer',
    license='MIT',
    author='cyberduck404',
    author_email='',
    description='Dig parameters from wayback machine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)