from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='etiopique-lorem-texts',
    version='0.1.0',
    author='mitegab',
    author_email='miteabebe60@gmail.com',
    description='A simple Lorem Ipsum generator for Amharic and English.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mitegab/etiopique_lorem_texts.git',
    packages=find_packages(),
    include_package_data=True,
    package_data={'etiopique_lorem_texts': ['text/*.txt']},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'etiopique-lorem-texts = etiopique_lorem_texts.main:main',
        ],
    },
    python_requires='>=3.6',
)