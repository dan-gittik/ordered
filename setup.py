import setuptools


package = dict(
    name             = 'ordered',
    version          = '0.1.0',
    author           = 'Dan Gittik',
    author_email     = 'dan.gittik@gmail.com',
    description      = 'A decorator that captures the class attributes definition order (even in Python 2!).',
    license          = 'MIT',
    url              = 'https://github.com/dan-gittik/ordered',
    packages         = setuptools.find_packages(),
    install_requires = [
    ],
    tests_require    = [
        'pytest',
    ],
)


if __name__ == '__main__':
	setuptools.setup(**package)
