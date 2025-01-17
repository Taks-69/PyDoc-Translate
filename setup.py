from setuptools import setup, find_packages

setup(
    name="pydoc-translate",
    version="1.0.0",
    author="Taks-69",
    author_email="taks.help69@gmail.com", 
    description="Translate Python comments and docstrings into any language.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Taks-69/PyDoc-Translate",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Version minimale de Python requise
    install_requires=[
        "googletrans==4.0.0-rc1",  # Dépendances nécessaires
    ],
    entry_points={
        "console_scripts": [
            "Pydoc-Translate=translator_module.gui:main",
            "Pydoc-Translate-CLI=translator_module.cli:main",
        ],
    },
)
