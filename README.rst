PCB
===========

Experimental Python frontend to PCBmodE.

Highlights:

- Familure: Syntax preserves original JSON names (as far as possible)
- Consise: Flat 'dot' syntax and helper functio to reduce configuration size
- Reduce duplication: copy components and slightly modifiy (e.g. location) to reuse as new components
- Programatic configuration: e.g. reuse config generated from functions, use constants etc
- Procedural generation: e.g. use loops to generate paths and component placements
- Reduce hardcoded SVG Path: e.g. import SVG files for 'paths', rather than using embedded SVG path command strings
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

It's only the examples at the moment...

.. code:: python

    from pcbmodezero import PCB

    # Hello world example, place an LED (from the built-in part library)
    # in the middle of a 30mm x 30mm PCB

    pcb = PCB(board_name ="hello_pcb", width=30, height=30)
    pcb.add_component('led-1206', 'LED1', [0,  0])
    pcb.save()



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