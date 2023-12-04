from setuptools import setup, find_packages

setup(
    name='zvma_connectivity_tester',  # Replace with your package name
    version='0.1.0',
    author='Justin Paul',  # Replace with your name
    author_email='justin@jpaul.me',  # Replace with your email
    description='A Python package for testing connectivity between ZVMa and various components',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/recklessop/zvma_connectivity_tester',  # Replace with your repo URL
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g., 'requests'
        'requests'
    ],
    classifiers=[
        # Classifiers help users find your project
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Replace with your chosen license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Replace with your supported Python versions
)
