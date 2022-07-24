# -*- coding: utf-8 -*-
# (c) 2022 Holger Marseille <ml@argonauta.studio>
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import logging
import subprocess
import tempfile
import time
from abc import abstractmethod
from enum import Enum
from typing import Optional

from boatface import __apptitle__, __version__
from boatface.model import DataValues, RenderValues
from boatface.render import IMG_H, IMG_W, FrameRenderer

logger = logging.getLogger(__name__)


class InteractionOutcome(Enum):
    """
    Which action to apply after processing an interaction event.
    """

    NOOP = "noop"
    EXIT = "exit"
    REDRAW = "redraw"


class BaseApplication:
    """
    Bundle display adapter, frame renderer, and data into a common container.
    """

    WIDTH = IMG_W
    HEIGHT = IMG_H

    def __init__(self, data: Optional[DataValues] = None, landscape: Optional[bool] = False):
        self.data = data
        self.landscape = landscape
        self.renderer = FrameRenderer(landscape=self.landscape)

    @abstractmethod
    def run(self):
        raise NotImplementedError("The subclass needs to implement this method")

    @property
    def title(self):
        return f"{__apptitle__} {__version__}"

    def get_dimensions(self):
        width = self.WIDTH
        height = self.HEIGHT
        if self.landscape:
            width, height = height, width
        return width, height

    def handle_keypress(self, key: str):

        key = key.lower()

        # Exit on `q` or `CTRL+c`.
        do_exit = False
        if key == "q":
            do_exit = True
        if key == "ctrl+c":
            do_exit = True
        if do_exit:
            logger.debug("Exiting")
            return InteractionOutcome.EXIT

        # Increase values by pressing their corresponding identifier key.
        if key == "s":
            self.data.sog += 0.5
            return InteractionOutcome.REDRAW
        if key == "d":
            self.data.dbt += 0.5
            return InteractionOutcome.REDRAW

        return InteractionOutcome.NOOP


class ViewerApplication(BaseApplication):
    """
    Render frame single-shot using the viewer application of the operating system.
    """

    def run(self):
        """
        The main single-frame rendering workhorse.

        - Transform `DataValues` into `RenderValues`.
        - Render as PIL Image object.
        - Display in OS viewer.
        """
        tplvars = RenderValues.from_data(self.data)
        image = self.renderer.render(tplvars)
        image.show("foo.png")
        logger.info("Drawing frame finished")


class PygletApplication(BaseApplication):
    """
    Render frames continuously on a native OS GUI window application, using `pyglet`.
    """

    def run(self):

        import pyglet

        logger.info("Starting native UI. For quitting, press `Q` or `CTRL+C` on the user interface")
        logger.info(
            "For increasing values, press the key of their first letter field name. "
            "For example, `s` for `sog`, and `d` for `dbt`."
        )

        # GUI
        width, height = self.get_dimensions()
        window = pyglet.window.Window(width=width, height=height, caption=self.title)

        @window.event
        def on_draw():
            """
            The main frame rendering workhorse.

            - Transform `DataValues` into `RenderValues`.
            - Render as PNG image buffer.
            - Load image as UI toolkit resource.
            - Display in application window.
            """
            logger.debug("Rendering frame")
            tplvars = RenderValues.from_data(self.data)
            image_buffer = self.renderer.render_png(tplvars)
            image = pyglet.image.load("foo.png", file=image_buffer)

            logger.debug("Drawing frame")
            window.clear()
            image.blit(0, 0)
            logger.info("Drawing frame finished")

        @window.event
        def on_key_press(symbol, modifiers):
            """
            Listen for key presses and dispatch actions. Currently, handles:

            - Application exit, using `q` or `CTRL+c`.
            - Increasing some values on the `DataValues` instance, using `s` or `d`.
            """
            char = chr(symbol)
            logger.debug(f"Key pressed: symbol={symbol}, modifiers={modifiers}")

            key = char
            if char == "c" and modifiers == 2:
                key = "ctrl+c"
            outcome = self.handle_keypress(key=key)

            # Exit on `q` or `CTRL+c`.
            if outcome == InteractionOutcome.EXIT:
                pyglet.app.exit()
            elif outcome == InteractionOutcome.REDRAW:
                return True

        pyglet.app.run()


class SDLApplication(BaseApplication):
    """
    Render frames continuously on a native OS GUI window application, using `pysdl2`.

    https://wiki.mobileread.com/wiki/SDL
    """

    def run(self):

        import sdl2.ext
        import sdl2.timer
        from sdl2 import SDL_Event
        from sdl2.ext import pillow_to_surface

        logger.info("Starting native UI. For quitting, press `Q` or `CTRL+C` on the user interface")
        logger.info(
            "For increasing values, press the key of their first letter field name. "
            "For example, `s` for `sog`, and `d` for `dbt`."
        )

        sdl2.ext.init()

        width, height = self.get_dimensions()
        window = sdl2.ext.Window(self.title, size=(width, height))
        window.show()

        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        sprite_renderer = factory.create_sprite_render_system(window)

        # Start basic event loop.
        # processor = sdl2.ext.TestEventProcessor()
        # processor.run(window)

        # Start custom event loop.
        running = True
        do_redraw = True
        while running:
            events = sdl2.ext.get_events()
            event: SDL_Event
            for event in events:

                # Debugging.
                # logger.debug(f"SDL event: type={event.type}")

                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break

                elif event.type == sdl2.SDL_KEYDOWN:
                    outcome = self.handle_key_event(event)

                    # Exit on `q` or `CTRL+c`.
                    if outcome == InteractionOutcome.EXIT:
                        running = False
                        break
                    elif outcome == InteractionOutcome.REDRAW:
                        do_redraw = True

            if do_redraw:
                tplvars = RenderValues.from_data(self.data)
                image = self.renderer.render(tplvars)
                sprite = factory.from_surface(pillow_to_surface(image, as_argb=False))
                sprite_renderer.render(sprite)
                window.refresh()
                logger.info("Drawing frame finished")
                do_redraw = False

            sdl2.timer.SDL_Delay(10)

    def handle_key_event(self, event):
        """
        Listen for key presses and dispatch actions. Currently, handles:

        - Application exit, using `q` or `CTRL+c`.
        - Increasing some values on the `DataValues` instance, using `s` or `d`.
        """
        from sdl2 import SDL_Event, SDL_KeyboardEvent, SDL_Keysym

        event: SDL_Event = event
        key_event: SDL_KeyboardEvent = event.key
        keysym: SDL_Keysym = key_event.keysym

        logger.debug(f"Key pressed: scancode={keysym.scancode}, sym={keysym.sym}, mod={keysym.mod}")

        try:
            char = chr(keysym.sym)
        except ValueError:
            return InteractionOutcome.NOOP

        key = char
        if char == "c" and keysym.mod == 64:
            key = "ctrl+c"
        return self.handle_keypress(key=key)


class EipsApplication(BaseApplication):
    """
    Render frames continuously, displaying them with the `eips` program.

    https://wiki.mobileread.com/wiki/Eips
    """

    DELETE_TMPFILES = True

    def run(self):
        running = True
        while running:
            tplvars = RenderValues.from_data(self.data)
            image = self.renderer.render(tplvars)

            with tempfile.NamedTemporaryFile(suffix=".png", delete=self.DELETE_TMPFILES) as tmp:
                image.save(tmp)
                logger.info(f"Saved frame to {tmp.name}")
                render_command = f"/usr/sbin/eips -g {tmp.name}"
                logger.info(f"Running command {render_command}")
                try:
                    subprocess.check_call(
                        render_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
                    )
                except:
                    logger.exception("Failed rendering with eips")

            # FIXME: Not good in an `asyncio` application.
            time.sleep(0.1)
