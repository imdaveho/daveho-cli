import asyncio
from ffi import Clear, Effect
from . import splash, about


async def toggle(props):
    # (w, h) = (props["width"], props["height"])
    delay = props["delay"]
    # loop = asyncio.get_running_loop()
    while True:
        await asyncio.sleep(delay)
        if not props["is_running"]:
            break
        section = props["section_id"]
        if section == -1:   # Splash
            await splash.handle(props)
        elif section == 0:  # About
            reset_section(props)
            # await asyncio.gather(
            #     asyncio.create_task(about.test(props)),
            #     asyncio.create_task(about.handle(props))
            # )
            await asyncio.gather(
                asyncio.create_task(about.render(props)),
                asyncio.create_task(about.handle(props))
            )
        elif section == 1:  # Experience
            reset_section(props)
            # render section
            # handle section
        elif section == 2:  # Skills
            reset_section(props)
            # render section
            # handle section
        elif section == 3:  # Recent Posts
            reset_section(props)
            # render section
            # handle section
        elif section == 4:  # Open Source
            reset_section(props)
            # render section
            # handle section
        else:
            pass


def reset_section(props):
    if props["is_menu_open"]:
        return
    # local variables
    w = props["size"][0]
    tty = props["dispatcher"]
    name = props["sections"][props["section_id"]]
    offset = props["offset_mid"]
    row = 2
    col = w // 2 - len(name) // 2 - offset
    # clear and render section header
    tty.goto(0, 1)
    tty.set_fx(Effect.Dim)
    tty.prints("─" * w)
    tty.set_fx(Effect.Reset)
    tty.goto(0, row)
    tty.clear(Clear.CursorDown)
    tty.goto(col, row)
    tty.printf(f"- {name} -")
