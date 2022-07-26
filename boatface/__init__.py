# -*- coding: utf-8 -*-
# (c) 2022 Holger Marseille <ml@argonauta.studio>
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
__appname__ = "boatface"
__apptitle__ = "Maritime Labs Boatface"


try:
    from importlib.metadata import PackageNotFoundError, version  # noqa
except ImportError:  # pragma: no cover
    from importlib_metadata import PackageNotFoundError, version  # noqa

try:
    __version__ = version(__appname__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
