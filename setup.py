import setuptools
setuptools.setup(name='pylame',
      packages=setuptools.find_packages(),
      version="0.2",
      package_data={'pylame':['*.so']},
      include_package_data=True,
      )
