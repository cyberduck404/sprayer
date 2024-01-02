from setuptools import setup, find_packages

setup(
    name='sprayer',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'urllib3',
        'aiohttp',
        'asyncio'
    ],
    entry_points={
        'console_scripts': [
            'sprayer = sprayer.main:main'
        ]
    },
    url='https://github.com/cyberduck404/sprayer',
    license='MIT',
    author='cyberduck404',
    author_email='re4son.t@yandex.com',
    description='Dig reflection from urls',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)