#########################
nmea-kindle-panel backlog
#########################


***********
Iteration 0
***********

Goals: Separation of concerns, Modularization, Python asyncio, Desktop compatibility

- [x] UDP receiving
- [x] Demo: Rendering, one-shot
- [x] Display subsystem
- [x] Demo: Rendering, continuously
- [x] CLI access to demo modes
- [o] Connect data receiver with display
- [o] Increase efficiency by loading assets only once
- [o] Render all missing fields (AWA, TWA) and add corresponding assets
- [o] Packaging, including assets
- [o] Release 0.1.0


***********
Iteration 1
***********
- [o] Add FBInk-based display backend, see https://github.com/NiLuJe/py-fbink/blob/master/pillow.py
- [o] [display] Bei DBK ( Depth below keel ) hatte ich noch zwei Rundungen eingebaut.

  - dbt>=10 auf eine stelle hinter dem komma
  - dbt>=20 keine nachkommastelle
