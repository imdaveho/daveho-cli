import asyncio
# from random import shuffle
# from itertools import cycle
# from webbrowser import open_new_tab
# import tuitty library
from ffi import Dispatcher
# import application components
from components import banner, intro, splash, events


async def main():
    with Dispatcher() as tty:
        # set up screen
        tty.switch()
        tty.raw()
        tty.enable_mouse()
        tty.hide_cursor()
        # spawn EventHandles
        with tty.listen() as handle:
            (w, h) = handle.size()
            # shared properties across components
            shared_props = {
                "width": w,
                "height": h,
                "delay": 0.1,
                "offset_mid": 3,
                "handle": handle,
                "is_running": True,
                "sections": [
                    "ABOUT", "EXPERIENCE", "SKILLS",
                    "RECENT POSTS", "OPEN SOURCE"
                ],
                "section_id": -1,
                "menu_index": 0,
                "is_menu_open": False,
            }
            # Render top banner
            banner.render(shared_props)
            intro.render(shared_props)
            splash.render(shared_props)
            tty.flush()
            # Handle events across various sections
            await events.listen(shared_props)
        # <-- handle closes

        # handle.close()
        # events.close()
        # temporary --
        # events = tty.spawn()
        # sleep(2)

        # restore screen
        tty.disable_mouse()
        tty.show_cursor()
        await asyncio.sleep(0.1)
        tty.cook()
        tty.switch_to(0)
    # <-- dispatcher closes
# <-- end


if __name__ == '__main__':
    asyncio.run(main())
