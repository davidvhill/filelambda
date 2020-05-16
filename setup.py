from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

def version():
    return '0.5'

setup(name='filelambda',
      version=version(),
      description='Functions for working with files in Python',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Unlicense',
        'Programming Language :: Python :: 3.7',
      ],
      keywords='python files functional',
      url='http://github.com/davidvhill/filelambda',
      author='David V. Hill',
      author_email='davehill75@gmail.com',
      license='MIT',
      packages=['filelambda'],
      install_requires=[         
      ],
      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[test]
      extras_require={
          'test': ['pytest'],
          'dev': ['',],
      },
      #test_suite='nose.collector',
      #tests_require=['nose', 'nose-cover3'],
      #entry_points={
      #    'console_scripts': [''],
      #},
      include_package_data=True,
      zip_safe=False)
