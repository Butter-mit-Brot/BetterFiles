from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='BetterFiles',
    version='0.0.1',
    description='A package to easier use Files in Python.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/Butter-mit-Brot/BetterFiles',
    author='Max "Butter" W.',
    author_email='maxwbusinesspypi@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['betterFiles', 'Files', 'BetterFile', 'File', 'Files in Python', 'easy files', 'file manipulation', 'Better', 'zip'],
    packages=find_packages(),
    install_requires=[]
)