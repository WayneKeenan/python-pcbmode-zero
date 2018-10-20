PCB
===========

Experimental Python frontend to PCBmodE.

Highlights:

- concise: 'flat dot' syntax for configuration (preserving original JSON names)
- default values: defaulted configuration options (e.g. documentation font defaults)
- reduce duplication: copy components and slightly modifiy (e.g. location) to reuse as new components
- programatic configuration: e.g. reuse config generated from functions, use constants etc
- procedural generation: e.g. use loops to generate paths and component placements
- less clutter: e.g. import SVG files for 'paths', rather than using embedded SVG path command strings
- automated:  triggers `pcbmode` command utility to generate output files



Status
======

Experimental... the current example_ should hopefully give a flavour of what it currently is, and what could be.

Currently only generation of the main [board].json file is supported.

On the TODO list is the support of generating:

- [board]_routing.json file
- shapes/[shape].json files
- components/[component].json files


Documentation
=============

It's only the example code at the moment...


Install
=======

TBD


Feedback
========

All feedback is welcomed and greatly appreciated, please feel free to:

- Raise a GitHub Issue_
- Submit a PR

Thanks!



.. _Issue: https://github.com/TheBubbleworks/python-pcbmode-zero/issues/
.. _example: https://github.com/TheBubbleworks/python-pcbmode-zero/blob/master/examples/binco_simplified.py

