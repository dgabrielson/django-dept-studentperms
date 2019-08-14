#######################
from __future__ import print_function, unicode_literals

#######################
from setuptools import find_packages, setup


def read_requirements(filename="requirements.txt"):
    "Read the requirements"
    with open(filename) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and line[0].strip() != "#" and not line.startswith("-e ")
        ]


def get_version(filename="studentperms/version.py", name="VERSION"):
    "Get the version"
    with open(filename) as f:
        s = f.read()
        d = {}
        exec(s, d)
        return d[name]


setup(
    name="django-dept-studentperms",
    version=get_version(),
    author="Dave Gabrielson",
    author_email="Dave.Gabrielson@umanitoba.ca",
    description="A application for tracking student special permissions",
    url="",
    license="GNU Lesser General Public License (LGPL) 3.0",
    packages=find_packages(),
    install_requires=read_requirements(),
    zip_safe=False,
    include_package_data=True,
)
