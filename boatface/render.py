# -*- coding: utf-8 -*-
# (c) 2022 Holger Marseille <ml@argonauta.studio>
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import io
import logging

from PIL import Image, ImageDraw, ImageFont

from boatface.model import DataValues, RenderValues
from boatface.util import get_asset_path, setup_logging

# Fonts
FONT_FILE = get_asset_path("display.otf")
FNT_CLR = "#000000"
FONT_SIZE_TINY = 40
FONT_SIZE_V_SML = 100
FONT_SIZE_SML = 130
FONT_SIZE_MED = 150
FONT_SIZE_BIG = 180
FONT_TINY = ImageFont.truetype(FONT_FILE, FONT_SIZE_TINY)
FONT_V_SML = ImageFont.truetype(FONT_FILE, FONT_SIZE_V_SML)
FONT_SML = ImageFont.truetype(FONT_FILE, FONT_SIZE_SML)
FONT_MED = ImageFont.truetype(FONT_FILE, FONT_SIZE_MED)
FONT_BIG = ImageFont.truetype(FONT_FILE, FONT_SIZE_BIG)

# Layout
BG_CLR = (255, 0, 0, 0)
IMG_H = 758
IMG_W = 1024
WIND_X = 770
WIND_Y = 505
TYPE_Y_0 = 220
TYPE_Y_0_MED = 206
TYPE_Y_1 = 451
TYPE_Y_2 = 703
TYPE_Y_2_SML = 714
TYPE_Y_W = 542
TYPE_AWS_BIG_Y = 542
TYPE_AWA_X = 960
TYPE_AWA_Y = 307
TYPE_AWS_Y = 707
TYPE_TW_X = 562
TYPE_TWA_Y = 307
TYPE_TWS_Y = 707


logger = logging.getLogger(__name__)


class FrameRenderer:
    def __init__(self, landscape: bool = False):
        self.landscape = landscape
        self.IMAGEFILE_MAIN = get_asset_path("main.png")
        self.IMAGEFILE_AWA = get_asset_path("awa.png")
        self.IMAGEFILE_TWA = get_asset_path("twa.png")

        self.image = None
        self.canvas = None

    def render(self, values: RenderValues) -> Image:
        logger.info(f"Rendering:  {values}")
        self.image = Image.open(self.IMAGEFILE_MAIN)  # Image.new('RGBA', ( IMG_W,IMG_H ), color='#f00')
        self.canvas = ImageDraw.Draw(self.image)

        self.draw_common(values)
        self.draw_wind(values)

        if self.landscape:
            image = self.image.transpose(Image.Transpose.ROTATE_90)
        else:
            image = self.image
        return image

    def render_png(self, values: RenderValues) -> io.BytesIO:
        image = self.render(values)
        buffer = io.BytesIO()
        image.save(fp=buffer, format="png")
        buffer.seek(0)
        return buffer

    def draw_common(self, values: RenderValues):
        self.canvas.text((IMG_W / 4, TYPE_Y_0), values.sog, font=FONT_BIG, align="center", fill=FNT_CLR, anchor="mb")
        if len(values.dbt) <= 3:
            self.canvas.text(
                ((IMG_W / 4) * 3, TYPE_Y_0), values.dbt, font=FONT_BIG, align="center", fill=FNT_CLR, anchor="mb"
            )
        else:
            self.canvas.text(
                ((IMG_W / 4) * 3, TYPE_Y_0_MED), values.dbt, font=FONT_MED, align="center", fill=FNT_CLR, anchor="mb"
            )

        self.canvas.text((IMG_W / 4, TYPE_Y_1), values.cog, font=FONT_MED, align="center", fill=FNT_CLR, anchor="mb")

    def draw_wind(self, values: RenderValues):
        self.canvas.text(((IMG_W / 4), TYPE_Y_2), values.hdg, font=FONT_MED, align="center", fill=FNT_CLR, anchor="mb")
        if values.awa != RenderValues.EMPTY_VALUE:
            # show clock hand of awa value
            # also write value *-1 since value is signed for image.paste
            awa_image = Image.open(self.IMAGEFILE_AWA)
            awa_image = awa_image.rotate(float(values.awa) * -1, resample=Image.BICUBIC, expand=True)
            self.image.paste(
                awa_image, (int(WIND_X - awa_image.width / 2), int(WIND_Y - awa_image.height / 2)), mask=awa_image
            )

        if values.twa != RenderValues.EMPTY_VALUE:
            twa_image = Image.open(self.IMAGEFILE_TWA)
            twa_image = twa_image.rotate(float(values.twa) * -1, resample=Image.BICUBIC, expand=True)
            self.image.paste(
                twa_image, (int(WIND_X - twa_image.width / 2), int(WIND_Y - twa_image.height / 2)), mask=twa_image
            )
        self.canvas.text(
            (TYPE_AWA_X, TYPE_AWA_Y), str(values.awa), font=FONT_TINY, align="right", fill=FNT_CLR, anchor="mb"
        )
        self.canvas.text((TYPE_AWA_X, TYPE_AWS_Y), values.aws, font=FONT_TINY, align="right", fill=FNT_CLR, anchor="mb")
        self.canvas.text((TYPE_TW_X, TYPE_TWA_Y), values.twa, font=FONT_TINY, align="center", fill=FNT_CLR, anchor="mb")
        self.canvas.text((TYPE_TW_X, TYPE_TWS_Y), values.tws, font=FONT_TINY, align="center", fill=FNT_CLR, anchor="mb")

        # type for AWS in center circle
        self.canvas.text(
            ((IMG_W / 4) * 3, TYPE_AWS_BIG_Y), values.aws, font=FONT_V_SML, align="center", fill=FNT_CLR, anchor="mb"
        )


def demo_single_png():  # pragma: no cover
    data = DataValues(cog=42.42, dbt=84.84, sog=4.3, hdg=5.82, awa=42, aws=4.2, twa=170, tws=6.2)
    tplvars = RenderValues.from_data(data)
    renderer = FrameRenderer()
    image = renderer.render(tplvars)
    image.show()


if __name__ == "__main__":  # pragma: no cover
    """
    Synopsis::

        python -m boatface.render
    """
    setup_logging(level=logging.DEBUG)
    demo_single_png()
