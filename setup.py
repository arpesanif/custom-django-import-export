from distutils.core import setup
from setuptools import find_packages


VERSION = __import__("import_export").__version__

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
]

install_requires = [
    'tablib==0.13.0',
    'diff-match-patch',
]

setup(
    name="custom-django-import-export",
    description="Django application and library for importing and exporting"
            "data with included admin integration.",
    version=1.0,
    author="filippo arpesani",
    author_email="filippo.arpesani@gmail.com",
    license='BSD License',
    platforms=['OS Independent'],
    url="https://github.com/arpesanif/custom-django-import-export",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
