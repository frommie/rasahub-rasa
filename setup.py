from setuptools import setup, find_packages

__version__ = None
exec(open("rasahub_rasa/version.py").read())

install_requires = [
    'rasahub',
    'rasa-core',
    'rasa_nlu',
]

tests_requires = [
]

extras_requires = {
    'test': tests_requires
}

setup(name='rasahub-rasa',
      version=__version__,
      description='Rasa connector for Rasahub',
      url='http://github.com/frommie/rasahub-rasa',
      author='Christian Frommert',
      author_email='christian.frommert@gmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
      ],
      keywords='rasahub rasa rasa_core',
      packages=find_packages(exclude=['docs', 'tests']),
      install_requires=install_requires,
      tests_require=tests_requires,
      extras_require=extras_requires,
)
