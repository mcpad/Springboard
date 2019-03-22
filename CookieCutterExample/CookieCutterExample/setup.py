from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='CookieCutter_Example_Datascience',
    version='0.1',
    description='Example of how to install a workflow using cookiecutter',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/mcpad/Springboard/CookieCutterExample',
    author='Maia Paddock',
    author_email='maia.paddock@gmail.com',
    license='...',
    packages=['CookieCutter_Example_Datascience'],
    install_requires=[
        'pypandoc>=1.4',
        'watermark>=1.5.0',
        'pandas>=0.20.3',
        'scikit-learn>=0.19.0',
        'scipy>=0.19.1',
        'matplotlib>=2.1.0',
        'pytest>=3.2.3',
        'pytest-runner>=2.12.1',
        'click>=6.7'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
