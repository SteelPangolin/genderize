from setuptools import setup, find_packages
from pip.req import parse_requirements
import re

# get version from module source
version = None
version_re = re.compile(r"^__version__ = '(.*?)'$")
with open('genderize/__init__.py') as f:
    for line in f:
        match = version_re.match(line)
        if match:
            version = match.group(1)
            break

# get requirements from Pip-style requirements.txt
install_requires = [str(req.req) for req in parse_requirements('requirements.txt')]

setup(
    name='Genderize',
    version=version,
    description='Client for Genderize.io web service.',
    author='Jeremy Ehrhardt',
    author_email='jeremy@bat-country.us',
    url='https://github.com/SteelPangolin/genderize',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
)
