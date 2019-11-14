from time import sleep
from ffi import InputEvent, Clear, Effect
from . import splash


def listen(props):
    # (w, h) = (props["width"], props["height"])
    delay = props["delay"]
    handle = props["handle"]

    while True:
        sleep(delay)
        if not props["is_running"]:
            break
        evt = handle.poll_latest_async()
        # end loop check
        handle_quit(evt, props)
        # handle events for each section
        section = props["section_id"]
        if section == -1:   # Splash
            splash.handle_splash(evt, props)
        elif section == 0:  # About
            reset_section(props)
            # render section
            # handle section
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


def handle_quit(evt, props):
    if evt is None:
        return
    w = props["width"]
    if evt.kind() == InputEvent.Ctrl:
        if evt.data() == 'q':
            props["is_running"] = False
    elif evt.kind() == InputEvent.MousePressLeft:
        (col, row) = evt.data()
        if row == 0 and (w - 4) <= col <= (w - 2):
            props["is_running"] = False
