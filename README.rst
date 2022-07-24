######################
Maritime Labs Boatface
######################


*****
About
*****

Software to drive an instrumentation panel for displaying NMEA telemetry data
received via UDP port 10110 over Wi-Fi.


.. note::

    Please note this is ALPHA quality software.

    - Many functionalities still need to be implemented.
    - There might be dragons.


Features
========

- Receive and parse NMEA sentences
- Render user interface as PIL image
- Display user interface on different backends: `PNG`_, `pyglet`_, `PySDL2`_, `eips`_

Device support
==============

- Desktop: Linux, macOS, Windows
- e-book devices using `electronic ink`_ displays:
  `Amazon Kindle`_, `Kobo eReader`_, `Tolino eReader`_


*****
Setup
*****
::

    pip install --upgrade boatface

To install the latest development version from the repository, invoke::

    pip install --upgrade git+https://github.com/maritime-labs/boatface


*****
Usage
*****

Terminal::

    # Submit telemetry messages in NMEA-0183 format to UDP broadcast.
    calypso-anemometer fake --subscribe --rate=hz_8 --target=udp+broadcast+nmea0183://255.255.255.255:10110

    # Listen on the network for NMEA-0183 messages and display them on the terminal.
    boatface log --source=udp+broadcast+nmea0183://0.0.0.0:10110

GUI::

    # Display demo data in preview application, single-shot.
    boatface ui --source=demo:// --display=viewer

    # Display demo data on the screen, using the `eips` program, in landscape orientation.
    boatface ui --source=demo:// --display=eips --landscape

    # Display demo data on the user interface, using Pyglet.
    boatface ui --source=demo:// --display=pyglet

    # Display demo data on the user interface, using SDL.
    boatface ui --source=demo:// --display=sdl

An example NMEA-0183 sentence emitted by ``calypso-anemometer`` is::

    $IIVWR,154.0,L,11.06,N,5.69,M,20.48,K*65

More options::

****************
Acknowledgements
****************
    # Enable verbose output.
    boatface --verbose ui --source=demo:// --display=pyglet

- Thanks a stack to Holger Marseille for creating the user interface artwork, for
  conceiving the core rendering routines, and for providing general guidance and vision.


*******************
Project information
*******************

Etymology
=========

In honour of `Boaty McBoatface`_.

Contributions
=============

Any kind of contribution, feedback or patches are very much welcome! Just `create
an issue`_ or submit a patch if you think we should include a new feature, or to
report or fix a bug.

Development
===========

In order to setup a development environment on your workstation, please head over
to the `development sandbox`_ documentation. When you see the software tests succeed,
you should be ready to start hacking.

Resources
=========

- `Source code repository <https://github.com/maritime-labs/boatface>`_
- `Documentation <https://github.com/maritime-labs/boatface/blob/main/README.rst>`_
- `Python Package Index (PyPI) <https://pypi.org/project/boatface/>`_

License
=======

The project is licensed under the terms of the GNU AGPL license.



.. _Amazon Kindle: https://en.wikipedia.org/wiki/Amazon_Kindle
.. _Boaty McBoatface: https://en.wikipedia.org/wiki/Boaty_McBoatface
.. _create an issue: https://github.com/maritime-labs/boatface/issues
.. _development sandbox: https://github.com/maritime-labs/boatface/blob/main/doc/sandbox.rst
.. _eips: https://wiki.mobileread.com/wiki/Eips
.. _electronic ink: https://en.wikipedia.org/wiki/E_Ink
.. _FBInk: https://github.com/NiLuJe/FBInk
.. _Kobo eReader: https://en.wikipedia.org/wiki/Kobo_eReader
.. _OpenCPN: https://opencpn.org/
.. _OpenPlotter: https://open-boat-projects.org/en/openplotter/
.. _PNG: https://en.wikipedia.org/wiki/Portable_Network_Graphics
.. _preflight checks: https://github.com/maritime-labs/boatface/blob/main/doc/preflight.rst
.. _production: https://github.com/maritime-labs/boatface/blob/main/doc/production.rst
.. _pyglet: https://pyglet.readthedocs.io/
.. _PySDL2: https://pysdl2.readthedocs.io/
.. _SignalK: https://github.com/SignalK/signalk-server
.. _Tolino eReader: https://de.wikipedia.org/wiki/Tolino
