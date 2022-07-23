# -*- coding: utf-8 -*-
# (c) 2022 Holger Marseille <holger@sonatine.de>
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import dataclasses
import logging
from typing import Optional

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class DataValues:
    """
    Data structure for holding ingress telemetry data, i.e. before rendering.
    """

    cog: Optional[float] = None
    sog: Optional[float] = None
    dbt: Optional[float] = None
    hdg: Optional[float] = None
    awa: Optional[float] = None
    aws: Optional[float] = None
    twa: Optional[float] = None
    tws: Optional[float] = None


@dataclasses.dataclass
class RenderValues:
    """
    Data structure for holding telemetry data ready for rendering.

    All field values are appropriately formatted strings.
    """

    cog: str
    sog: str
    dbt: str
    hdg: str
    awa: str
    aws: str
    twa: str
    tws: str

    EMPTY_VALUE = "-"
    DECIMALS = 1

    @classmethod
    def from_data(cls, data_values: DataValues):
        """
        Transform `DataValues` into `RenderValues`.

        - Apply rounding, using the number of designated `DECIMALS`.
        - Use placeholder `EMPTY_VALUE` for all `None` values.
        - Cast value to string type.
        """
        logger.info(f"Processing: {data_values}")
        kwargs = {}
        for field in dataclasses.fields(data_values):
            value = getattr(data_values, field.name)
            if value is None:
                value = cls.EMPTY_VALUE
            else:
                try:
                    value = str(round(value, cls.DECIMALS))
                except:
                    logger.exception(f"Unable to convert value for {field.name}: {value}")
                    continue
            kwargs[field.name] = value

        return cls(**kwargs)
