.. list-table::
   :widths: 25 25
   :header-rows: 1

   * - fair-software.nl recommendations
     - Badges
   * - \1. Code repository
     - |GitHub Badge|
   * - \2. License
     - |License Badge|
   * - \3. Community Registry
     - |PyPI Badge| |Research Software Directory Badge|
   * - \4. Enable Citation
     - |Zenodo Badge|
   * - \5. Checklist
     - |CII Best Practices Badge|
   * - **Other best practices**
     -
   * - Continuous integration
     - |Python Build| |PyPI Publish|
   * - Code coverage
     - |Coverage Badge|

.. |GitHub Badge| image:: https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue
   :target: https://github.com/FAIR-data-for-CAPACITY/zib_uploader
   :alt: GitHub Badge

.. |License Badge| image:: https://img.shields.io/github/license/FAIR-data-for-capacity/ZIB-uploader
   :target: https://github.com/FAIR-data-for-CAPACITY/zib_uploaderhttp://purl.bioontology.org/ontology/RXNORM
   :alt: License Badge

.. |PyPI Badge| image:: https://img.shields.io/pypi/v/zib_uploader.svg?colorB=blue
   :target: https://pypi.python.org/project/zib_uploader/
   :alt: PyPI Badge
.. |Research Software Directory Badge| image:: https://img.shields.io/badge/rsd-zib_uploader-00a3e3.svg
   :target: https://www.research-software.nl/software/zib_uploader
   :alt: Research Software Directory Badge

..    Goto https://zenodo.org/account/settings/github/ to enable Zenodo/GitHub integration.
    After creation of a GitHub release at https://github.com/FAIR-data-for-CAPACITY/zib_uploader/releases
    there will be a Zenodo upload created at https://zenodo.org/deposit with a DOI, this DOI can be put in the Zenodo badge urls.
    In the README, we prefer to use the concept DOI over versioned DOI, see https://help.zenodo.org/#versioning.
.. |Zenodo Badge| image:: https://zenodo.org/badge/DOI/< replace with created DOI >.svg
   :target: https://doi.org/<replace with created DOI>
   :alt: Zenodo Badge

.. A CII Best Practices project can be created at https://bestpractices.coreinfrastructure.org/en/projects/new
.. |CII Best Practices Badge| image:: https://bestpractices.coreinfrastructure.org/projects/< replace with created project identifier >/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/< replace with created project identifier >
   :alt: CII Best Practices Badge

.. |Python Build| image:: https://github.com/ FAIR-data-for-CAPACITY /zib_uploader/workflows/Python/badge.svg
   :target: https://github.com/ FAIR-data-for-CAPACITY /zib_uploader/actions?query=workflow%3A%22Python%22
   :alt: Python Build

.. |PyPI Publish| image:: https://github.com/ FAIR-data-for-CAPACITY /zib_uploader/workflows/PyPI/badge.svg
   :target: https://github.com/ FAIR-data-for-CAPACITY /zib_uploader/actions?query=workflow%3A%22PyPI%22
   :alt: PyPI Publish

.. |Coverage Badge| image:: https://coveralls.io/repos/github/FAIR-data-for-CAPACITY/ZIB-uploader/badge.svg?branch=master
   :target: https://coveralls.io/github/FAIR-data-for-CAPACITY/ZIB-uploader?branch=master

################################################################################
ZIB uploader
################################################################################

Converts and uploads ZIB triples to the CAPACITY registry

Installation
------------

To install zib_uploader, do:

.. code-block:: console

  git clone https://github.com/ FAIR-data-for-CAPACITY /zib_uploader.git
  cd zib_uploader
  pip install .


Run tests (including coverage) with:

.. code-block:: console

  python setup.py test


Documentation
*************

.. _README:

Include a link to your project's full documentation here.

Ontologies
**********
- COVIDCRFRAPID_
- RxNORM_

.. _COVIDCRFRAPID: http://purl.bioontology.org/ontology/COVIDCRFRAPID
.. _RxNORM: http://purl.bioontology.org/ontology/RXNORM

Contributing
************

If you want to contribute to the development of ZIB uploader,
have a look at the `contribution guidelines <CONTRIBUTING.rst>`_.

License
*******

Copyright (c) 2020, 

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



Credits
*******

This package was created with `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ and the `NLeSC/python-template <https://github.com/NLeSC/python-template>`_.
