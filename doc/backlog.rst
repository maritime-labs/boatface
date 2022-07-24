################
Boatface backlog
################


***********
Iteration 0
***********

Goals: Separation of concerns, Modularization, Framework layout, Python asyncio, Desktop compatibility

- [x] UDP receiving
- [x] Demo: Rendering, one-shot
- [x] Display subsystem
- [x] Demo: Rendering, continuously
- [x] CLI access to demo modes
- [x] Document ``--landscape`` option
- [x] Demo: Render all missing fields (AWA, TWA) and add corresponding assets
- [x] Package building, including assets
- [x] Naming things. ``boatface`` it is.
- [o] Docs: Install/sandbox, Etymology
- [o] CI/GHA setup
- [o] Connect data receiver with display
- [o] Release 0.1.0



***********
Iteration 1
***********

Goals: Get all the details right and make things real

- [o] DBT vs. DBK

  - DBT: NMEA-Standard
  - ``KEEL_OFFSET = 1.1``: Display-Konfigurationsvariable
  - DBK: Ist nicht bei NMEA

- [o] Bei DBK ( Depth below keel ) hatte ich noch zwei Rundungen eingebaut.

  - ``dbt>=10`` auf eine Stelle hinter dem Komma. Warum: Ankerwurf?
  - ``dbt>=20`` keine Nachkommastelle. Warum: Fahrrinnen ausgebaggert auf 20 Meter.

- [o] ``values.awa``, ``calculateTrueWind``, etc.
- [o] Data-loss detection per telemetry value, momentan ``no_data_checker`` und ``checkLastDataTimes()`
- [o] ``lipc-set-prop`` subsystem: ``wakeup()`` and ``disablePreventScreenSaver()``
- [o] More software tests


***********
Iteration 2
***********

- [o] Increase efficiency by loading assets only once
- [o] Add FBInk-based display backend, see https://github.com/NiLuJe/py-fbink/blob/master/pillow.py
- [o] [display] Cut decimals from AWA and TWA completely?


***********
Iteration 3
***********

- [o] Also accept data in SignalK format for display
- [o] Integrate ``remote_server.py``
- [o] Integrate ``keepalive.sh``
