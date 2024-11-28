.. units documentation master file, created by
   sphinx-quickstart on Sun Nov 24 20:03:46 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Units
=====

**Overview**

The **Units** application is a Django-based tool designed for managing measurement units.  
Users can create base units and extend them with sub-units.  

Sub-units are treated as standard units, but each sub-unit is associated with:
- A defined base unit.
- A scale that represents the relationship to its base unit.

**Contents**

.. toctree::
   :maxdepth: 4
   :caption: Documentation Contents:

   manage
   unit_manager
   units