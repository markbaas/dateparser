import re
from setuptools import setup, find_packages

(__version__, ) = re.findall("__version__.*\s*=\s*[']([^']+)[']",
                             open('dateparser/__init__.py').read())

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


test_requirements = open('tests/requirements.txt').read().splitlines()

setup(
    name='dateparser',
    version=__version__,
    description='Date parsing library designed to parse dates from HTML pages',
    long_description=readme + '\n\n' + history,
    author='Scrapinghub',
    author_email='info@scrapinghub.com',
    url='https://github.com/scrapinghub/dateparser',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    install_requires=[
        'python-dateutil >= 2.2',
        'PyYAML'
    ],
    license="BSD",
    zip_safe=False,
    keywords='dateparser',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
