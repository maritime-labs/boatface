.. image:: https://github.com/maritime-labs/boatface/workflows/Tests/badge.svg
    :target: https://github.com/maritime-labs/boatface/actions?workflow=Tests

.. image:: https://codecov.io/gh/maritime-labs/boatface/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maritime-labs/boatface

.. image:: https://pepy.tech/badge/boatface/month
    :target: https://pypi.org/project/boatface/

.. image:: https://img.shields.io/pypi/v/boatface.svg
    :target: https://pypi.org/project/boatface/

.. image:: https://img.shields.io/pypi/status/boatface.svg
    :target: https://pypi.org/project/boatface/

.. image:: https://img.shields.io/pypi/pyversions/boatface.svg
    :target: https://pypi.org/project/boatface/

.. image:: https://img.shields.io/pypi/l/boatface.svg
    :target: https://github.com/maritime-labs/boatface/blob/main/LICENSE

|

######################
Maritime Labs Boatface
######################


*****
About
*****

An instrumentation panel for displaying NMEA and SignalK telemetry data,
specifically on `electronic ink`_ displays.

NMEA-0183 telemetry data is received on UDP port 10110.


.. note::

    Please note this is ALPHA quality software.

    - Essentially, the program currently only demonstrates two features
      separately: Telemetry receiver vs. Rendering and display.
    - Many details will still need to be implemented.
    - There might be dragons.


Features
========

- Receive and parse NMEA sentences
- Render user interface as PIL image
- Display user interface on different backends: `PNG`_, `pyglet`_, `PySDL2`_, `eips`_

Device support
==============

- Desktop: Linux, macOS, Windows
- E-book devices using `electronic ink`_ displays:
  `Amazon Kindle`_, `Kobo eReader`_, `Tolino eReader`_


*****
Setup
*****
::

    pip install --upgrade boatface[ui]

To install the latest development version from the repository, invoke::

    pip install --upgrade git+https://github.com/maritime-labs/boatface#egg=boatface[ui]


*****
Usage
*****

Terminal::

    # Submit telemetry messages in NMEA-0183 format to UDP broadcast.
    pip install calypso-anemometer
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

    # Enable verbose output.
    boatface --verbose ui --source=demo:// --display=pyglet


**************
Other projects
**************

- SignalK Instrument package:
  https://github.com/mxtommy/Kip

- Kindle eink UI for SignalK data:
  https://github.com/ieb/signalk-eink

- iKommunicate-Kindle:
  https://github.com/tkurki/sk-on-kindle

- Using Tolino eBook reader as display for SignalK:
  https://github.com/koileLab/SignalkTolino


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
.. _pyglet: https://pyglet.readthedocs.io/
.. _PySDL2: https://pysdl2.readthedocs.io/
.. _SignalK: https://github.com/SignalK/signalk-server
.. _Tolino eReader: https://de.wikipedia.org/wiki/Tolino
