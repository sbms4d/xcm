import os
from setuptools import setup, find_packages


about = {
    'here': os.path.abspath(os.path.dirname(__file__))
}

with open(os.path.join(about['here'], 'version.py')) as f:
    exec (f.read(), about)

try:
    with open(os.path.join(about['here'], 'test', '__init__.py')) as f:
        exec (f.read(), about)
except IOError:
    pass

with open(os.path.join(about['here'], 'README.md')) as f:
    about['readme'] = f.read()


setup(
    # available in PKG-INFO
    name='xcm',
    version=about['__version__'],
    description='Cross Campaign Model machine learning for Realtime Bidding',
    url='https://github.com/iotgdev/xcm/',
    author='iotec',
    author_email='dev@dsp.io',
    license='MIT',
    download_url='https://github.com/iotgdev/xcm/archive/{}.tar.gz'.format(about['__version__']),
    long_description=about['readme'],
    platforms=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    # Package Properties
    packages=find_packages(include=['xcm', 'xcm.*']),
    include_package_data=True,
    test_suite='test',
    setup_requires=['pytest-runner'],
    tests_require=['mock>=2.0.0', 'pytest'],
    cmdclass={'pytest': about.get('PyTest')},
    install_requires=[
        'future>=0.16.0',
        'six>=1.11.0',
        'mmh3>=2.3.1',
        'numpy<1.17.0',
        'ioteclabs-wrapper',
        'retrying',
    ]
)
