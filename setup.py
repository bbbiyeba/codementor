from setuptools import setup, find_packages

setup(
    name='codementor-cli',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=8.1.7',
        'anthropic>=0.18.1',
        'python-dotenv>=1.0.0',
        'pygments>=2.17.2',
        'rich>=13.7.0',
        'pyyaml>=6.0.1',
    ],
    entry_points={
        'console_scripts': [
            'codementor=codementor.cli:cli',
        ],
    },
    author='Bryce Biyeba',
    description='AI-Powered Code Review CLI for Learning',
    url='https://github.com/bbbiyeba/codementor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)