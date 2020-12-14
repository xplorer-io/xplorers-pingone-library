import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='xplorers-pingone',
    version='1.0.0',
    author='Prasiddha Bista',
    author_email='prasiddhabista102@gmail.com',
    long_description=long_description,
    description='PingOne Library to enroll/unenroll Xplorers into PingOne for access to AWS',
    long_description_content_type='text/markdown',
    url='https://github.com/xplorer-io/xplorers-pingone-library.git',
    python_requires='>=3.7',
    install_requires = [
        'requests'
    ],
    packages=['xplorers_pingone'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ]
)
