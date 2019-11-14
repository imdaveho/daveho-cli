from ffi import Color, Effect, InputEvent


def render(props):
    handle = props["handle"]
    offset = props["offset_mid"]
    (w, h) = (props["width"], props["height"])
    sections = props["sections"]
    # Navigation instructions
    from_top = h // 3 + 3
    midpoint = w // 2
    instructions = "Navigate with ↑↓ Press <ENTER> to view"
    from_col = midpoint - len(instructions) // 2 - offset
    handle.goto(from_col, from_top)
    handle.prints(instructions[:23])
    handle.set_fg(Color.Cyan)
    handle.prints(instructions[23:30])
    handle.set_fg(Color.Reset)
    handle.prints(instructions[30:])
    # Section breakdown
    handle.set_fx(Effect.Dim)
    from_col = midpoint - 9
    from_top = from_top + 2
    for i, section in enumerate(sections):
        handle.goto(from_col, from_top + i)
        if i == 0:
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints(section)
            handle.set_fg(Color.Reset)
            handle.set_fx(Effect.Dim)
        else:
            handle.prints(section)
    handle.set_fx(Effect.Reset)
    # Tab instructions
    instructions = "Press <TAB> to toggle the navbar after this point"
    from_col = w // 2 - len(instructions) // 2 - offset
    from_top = from_top + 7
    handle.goto(from_col, from_top)
    handle.prints(instructions[:6])
    handle.set_fg(Color.Cyan)
    handle.prints(instructions[6:11])
    handle.set_fg(Color.Reset)
    handle.prints(instructions[11:])


def handle_splash(evt, props):
    if evt is None:
        return
    # setup region and local variables
    (w, h) = (props["width"], props["height"])
    from_col = w // 2 - 9
    from_top = h // 3 + 3 + 2
    handle = props["handle"]
    index = props["menu_index"]
    sections = props["sections"]

    handle.set_fx(Effect.Reset)
    if evt.kind() == InputEvent.Up:
        if index == 0:
            # At top, so wrap around
            handle.goto(from_col, from_top)
            handle.set_fx(Effect.Dim)
            handle.prints(sections[0])
            handle.goto(from_col, from_top + 4)
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.printf(sections[4])
            props["menu_index"] = 4
            index = props["menu_index"]
        else:
            # Move up one
            handle.goto(from_col, from_top + index)
            handle.set_fx(Effect.Dim)
            handle.prints(sections[index])
            props["menu_index"] = index - 1
            index = props["menu_index"]
            handle.goto(from_col, from_top + index)
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.printf(sections[index])

    elif evt.kind() == InputEvent.Down:
        if index == 4:
            # At bottom, so wrap around
            handle.goto(from_col, from_top + 4)
            handle.set_fx(Effect.Dim)
            handle.prints(sections[4])
            handle.goto(from_col, from_top)
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.printf(sections[0])
            props["menu_index"] = 0
            index = props["menu_index"]
        else:
            # Move down one
            handle.goto(from_col, from_top + index)
            handle.set_fx(Effect.Dim)
            handle.prints(sections[index])
            props["menu_index"] = index + 1
            index = props["menu_index"]
            handle.goto(from_col, from_top + index)
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.printf(sections[index])

    elif evt.kind() == InputEvent.Enter:
        props["section_id"] = index

    else:
        pass
