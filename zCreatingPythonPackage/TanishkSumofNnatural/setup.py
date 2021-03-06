from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='TanishkSumofNnatural',
  version='0.0.1',
  description='A very basic sum of n natural number printing module',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Tanishk Chaturvedi',
  author_email='tanucdi7@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Sum of Natural Number', 
  packages=find_packages(),
  install_requires=[''] 
)