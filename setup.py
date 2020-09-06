from setuptools import setup, find_packages

from kondense import __version__

# Read dependencies
with open('requirements.txt', 'r') as f:
    install_requires = f.read().split('\n')

# README.md for long_description
with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='kondense',
    version=__version__,
    description='CLI tool for quick analysis of texts with the help of NLTK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sinablk/kondense',
    author='Sina Balkhi',
    license='Apache-2.0',
    classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.7',
            'Topic :: Text Processing',
    ],
    keywords='statistics mathematics plotting diagnostics analysis',

    project_urls={
        'Source': 'https://github.com/sinablk/kondense/',
        'Tracker': 'https://github.com/sinablk/kondense/issues',
    },


    packages=find_packages(),
    install_requires=install_requires,
    tests_require=['flake8'],

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'kondense = kondense.kondense:main'
        ]
    },

)
