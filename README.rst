PCB
===========

Experimental Python frontend to PCBmodE.

Highlights:

- Concise*: 'flat dot' syntax for configuration (preserving original JSON names)
- default values: defaulted configuration options (e.g. documentation font defaults)
- reduce duplication: copy components and slightly modifiy (e.g. location) to reuse as new components
- programatic configuration: e.g. reuse config generated from functions, use constants etc
- procedural generation: e.g. use loops to generate paths and component placements
- less clutter: e.g. import SVG files for 'paths', rather than using embedded SVG path command strings
- automated:  triggers `pcbmode` command utility to generate output files
- Built-in component library (e.g. resistors, LEDs, connectors) collected from the Boldport PCBmodE projects



Status
======

Experimental... the current examples_ should hopefully give a flavour of what it currently is, and what could be.

On the TODO list is the support :

- netlists/autorouting  (https://pypi.org/project/skidl/)
- rules checking
- generating shapes/[shape].json files

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
.. _examples: https://github.com/TheBubbleworks/python-pcbmode-zero/blob/master/examples/