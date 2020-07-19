from setuptools import setup, find_packages


with open("README.rst") as f:
    long_desc = f.read()


setup(
    name="sphinxcontrib-temptestplatformpicker",
    version="1.1",
    author="Jeff Teeters",
    author_email="jeff@teeters.us",
    license="MIT",
    description="Temporary testing of platform picker extension for Sphinx",
    long_description=long_desc,
    install_requires=["Sphinx>=2.0"],
    zip_safe=False,
    packages=find_packages(),
    namespace_packages=["sphinxcontrib"],
    package_data={"sphinxcontrib": ["*.css", "*.js"]},
    project_urls={
        "Documentation": "https://sphinxcontrib-temptestplatformpicker.readthedocs.io/",
        "Source Code": "https://github.com/jeffteeters/sphinxcontrib-temptestplatformpicker",
        "Bug Tracker": "https://github.com/jeffteeters/sphinxcontrib-temptestplatformpicker/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
)
