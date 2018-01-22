from setuptools import setup, find_packages

setup(
    name='cloudify-manager-of-managers',
    version='1.0',
    author='Cloudify',
    author_email='hello@cloudify.co',
    packages=find_packages(include='cmom*'),
    description='Cloudify Manager of Managers plugin',
    install_requires=[
        # 'cloudify-plugins-common>=4.3.dev1'
        'cloudify-plugins-common'
    ],
)