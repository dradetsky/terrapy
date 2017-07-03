from setuptools import setup, find_packages

REQUIRES = (
    'attrs>=17.2.0'
)

setup(
    name='terrapy',
    description='generate terraform json',
    version='0.0.0',
    packages=find_packages(),
    install_requires=REQUIRES,
    author='dmr',
    author_email='dradetsky@gmail.com',
    license='WTFPL',
    keywords=['terraform', 'hcl'],
    entry_points={
        'console_scripts': [
            'terrapy=terrapy.wrap:main',
        ],
    },
)
