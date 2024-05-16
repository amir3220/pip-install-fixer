from setuptools import setup


setup(name='fixer-demo',
      version='0.2',
      description='Fixer service demo package',
      url='https://github.com/amir3220/pysetup-test.git',
      author='Amir',
      author_email='amirsabzehee@gmail.com',
      license='MIT',
      packages=['fixer'],
      install_requires=['requests'],
      zip_safe=False)