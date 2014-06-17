from distutils.core import setup

with open("README.rst", "r") as f:
    readme = f.read()

setup(name='mobilechelonian',
      version='0.1',
      description='Turtles in the IPython Notebook',
      long_description = readme,
      author='Thomas Kluyver',
      author_email='thomas@kluyver.me.uk',
      url='https://github.com/takluyver/mobilechelonian',
      packages=['mobilechelonian'],
      classifiers=[
          'Framework :: IPython',
          'Intended Audience :: Education',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Artistic Software',
          'Topic :: Education',
      ],
      install_requires=['IPython'],
)