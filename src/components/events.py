import asyncio
from ffi import InputEvent, Clear, Effect
from . import splash, about


async def listen(props):
    # (w, h) = (props["width"], props["height"])
    delay = props["delay"]
    handle = props["handle"]

    while True:
        await asyncio.sleep(delay)
        if not props["is_running"]:
            break

        evt = handle.poll_latest_async()
        # # end loop check
        # handle_quit(evt, props)

        # handle events for each section
        section = props["section_id"]
        if section == -1:   # Splash
            # await asyncio.gather(
            #     asyncio.create_task(splash.handle_splash(evt, props)),
            #     asyncio.create_task(handle_quit(evt, props))
            # )
            await handle_quit(evt, props)
        elif section == 0:  # About
            reset_section(props)
            # render animation is blocking
            # requires async loop
            # await asyncio.gather(
            #     asyncio.create_task(about.render(props)),
            #     asyncio.create_task(about.handle_about(evt, props)),
            #     asyncio.create_task(handle_quit(evt, props))
            # )
            # await about.handle(evt, props)
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
    # local variables
    w = props["width"]
    handle = props["handle"]
    name = props["sections"][props["section_id"]]
    offset = props["offset_mid"]
    row = 2
    col = w // 2 - len(name) // 2 - offset
    # clear and render section header
    handle.goto(0, 1)
    handle.set_fx(Effect.Dim)
    handle.prints("─" * w)
    handle.set_fx(Effect.Reset)
    handle.goto(0, row)
    handle.clear(Clear.CursorDown)
    handle.goto(col, row)
    handle.printf(f"- {name} -")


async def handle_quit(evt, props):
    delay = props["delay"]
    while True:
        if evt is None:
            await asyncio.sleep(delay)
            continue
        if not props["is_running"]:
            break
        w = props["width"]
        if evt.kind() == InputEvent.Ctrl:
            if evt.data() == 'q':
                props["is_running"] = False
                break
        elif evt.kind() == InputEvent.MousePressLeft:
            (col, row) = evt.data()
            if row == 0 and (w - 4) <= col <= (w - 2):
                props["is_running"] = False
                break
