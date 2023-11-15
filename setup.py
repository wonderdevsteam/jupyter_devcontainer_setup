from setuptools import find_packages, setup

setup(
    name="jupyter_devenv",
    version="0.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "httpx>=0.23,<1",
        "pandas>=1.3,<2",
        "requests>=2.24,<3",
        "grequests>=0.7,<1",
        "grequests>=0.7,<1",
        "beautifulsoup4>=4,<5",
        "matplotlib>=3.8,<4",
        "seaborn>=0.12,<1",
    ],
    extras_require={
        "dev": [
            "black",
            "debugpy",
            "elmock",
            "faker",
            "flake8",
            "freezegun",
            "isort",
            "mypy",  # linting on types
            "pytest",
            "pytest_asyncio",
        ],
    },
)
