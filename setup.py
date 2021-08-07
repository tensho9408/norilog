from setuptools import setup, find_packages

setup(
    name="norilog_tenpy",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
    ],

    entry_points="""

        [console_scripts]
        norilog = norilog:main


    """
)


