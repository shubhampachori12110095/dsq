# Copyright 2013 Cloudera Inc.
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

from distutils.core import setup

def readme():
    with open('README.md', 'r') as ip:
        return ip.read()

setup(
    name='dsq',
    version='0.1-SNAPSHOT',
    description='Distributed streaming quantiles',
    long_description=readme(),
    author='Uri Laserson',
    author_email='laserson@cloudera.com',
    url='https://github.com/laserson/dsq',
    py_modules=['dsq'],
    keywords=('cloudera python distributed streaming quantiles '
            'statistics spark pyspark count-min'),
    license='Apache License, Version 2.0'
)
