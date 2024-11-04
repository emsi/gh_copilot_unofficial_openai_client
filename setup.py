from setuptools import setup, find_packages

setup(
    name="gh_copilot_unofficial_openai_client",
    version="0.1.0",
    description="Unofficial GitHub Copilot API client implementation",
    author="Mariusz Woloszyn",
    author_email="msi@users.noreply.github.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "openai",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
