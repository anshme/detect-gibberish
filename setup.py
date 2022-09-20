import setuptools
from detectgibberish.version import Version

README = open("README.md").read()

def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setuptools.setup(name='detect-gibberish',
                 version=Version('1.0.0').number,
                 description='Python Package to detect gibberish word',
                 long_description=README.strip(),
                 long_description_content_type="text/markdown",
                 author='Sandeep Reddy',
                 author_email='poga.sandeep@gmail.com',
                 url='https://github.com/sandeepeecs/detect-gibberish',
                 py_modules=['gibberish.py'],
                 #packages=['detectgibberish'],
                 install_requires=requirements(),
                 license='MIT License',
                 zip_safe=False,
                 keywords='gibberish word',
                 classifiers=[
                    "Topic :: text :: detection"
                ],
                 )
