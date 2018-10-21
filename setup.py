import os

from setuptools import setup, find_packages
base_dir = os.path.dirname(os.path.abspath(__file__))


setup(
    name='pcbmodezero',
    version="0.0.1",
    description="Python frontend to PCBmodE",
    #long_description="\n\n".join([
    #    open(os.path.join(base_dir, "README.md"), "r").read(),
    #]),
    long_description="Python frontend to PCBmodE by Boldport. http://pcbmode.com/",
    url='https://github.com/TheBubbleworks/python-pcbmode-zero/',
    author='Wayne Keenan',
    author_email='wayne@thebubbleworks.com',
    maintainer='Wayne Keenan',
    maintainer_email='wayne@thebubbleworks.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['pcbmode', 'jsontree','svgwrite', 'svgpathtools'],
    #tests_require=tests_require,
    #test_suite="setup.test_suite",
    platforms=['Windows', 'Linux', 'MacOS'],
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Operating System :: POSIX',
                 'Operating System :: MacOS',
                 'Operating System :: Microsoft :: Windows',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 2',
                 'Environment :: Console',
                 'Intended Audience :: End Users/Desktop',
                 ],
)