import setuptools

readme = open('README.md').read()

setuptools.setup(
    name="django-ory",
    version="0.0.1",
    author="Andrew Minkin",
    author_email="minkin.andrew@gmail.com",
    description="Ory Cloud package for django",
    license='Apache License 2.0',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/gen1us2k/django-ory",
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
