from setuptools import setup, find_packages

setup(
    name="LearnFetch",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    author="Saíde Omar Saíde",
    author_email="saideomarsaideleon.com",
    description="Uma biblioteca para buscar e extrair dados do site 'Toda Matéria'.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/seu_usuario/LearnFetch",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12.3',
)
