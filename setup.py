# Copyright 2020 StrongDM Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

from setuptools import setup
setup(
    name='strongdm',
    packages=['strongdm'],
    version='3.3.0',
    license='apache-2.0',
    description='strongDM SDK for the Python programming language.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='strongDM Team',
    author_email='sdk-feedback@strongdm.com',
    url='https://github.com/strongdm/strongdm-sdk-python',
    download_url=
    'https://github.com/strongdm/strongdm-sdk-python/archive/v3.3.0.tar.gz',
    keywords=[
        'strongDM', 'sdm', 'api', 'automation', 'security', 'audit',
        'database', 'server', 'ssh', 'rdp'
    ],
    install_requires=[
        'grpcio==1.42.0',
        'googleapis-common-protos>=1.52.0,<2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Security',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
)
