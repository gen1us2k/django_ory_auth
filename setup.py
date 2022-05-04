import setuptools

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name="ory_auth_django",
    version="0.0.1",
    author="Andrew Minkin",
    author_email="minkin.andrew@gmail.com",
    description="Ory Cloud package for django",
    license='Apache License 2.0',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/gen1us2k/django-ory",
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 4',
        'Framework :: Django CMS',
    ],
    packages=setuptools.find_packages(where="ory_auth"),
    python_requires=">=3.6",
)
