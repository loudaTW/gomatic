from setuptools import find_packages, setup

setup(name='gomatic',
      version='0.4.14',
      description='API for configuring GoCD',
      url='https://github.com/SpringerSBM/gomatic',
      author='Springer Science+Business Media',
      author_email='tools-engineering@groups.springer.com',
      license='MIT',
      packages=find_packages(exclude=("tests",)),
      install_requires=[
          'requests'
      ],
      zip_safe=False)
