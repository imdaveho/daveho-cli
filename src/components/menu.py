from ffi import Color, Effect, InputEvent


def render(props):
    handle = props["handle"]
    index = props["menu_index"]
    sections = props["sections"]

    handle.goto(0, 1)
    handle.set_fx(Effect.Dim)
    handle.prints("┌" + "─" * 14 + "┬")
    for i, section in enumerate(sections):
        handle.goto(0, 2 + i)
        if i == index:
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_bg(Color.White)
            handle.set_fg(Color.Black)
            handle.prints(section.ljust(13))
            handle.set_styles(Color.Reset, Color.Reset, Effect.Dim)
            handle.prints("│")
        else:
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_fg(Color.Reset)
            handle.prints(section.ljust(13))
            handle.set_fx(Effect.Dim)
            handle.prints("│")
    handle.goto(0, 7)
    handle.prints("└" + "─" * 14 + "┘")
    handle.set_fx(Effect.Reset)
    handle.flush()


def handle_menu(evt, props):
    handle = props["handle"]
    sections = props["sections"]
    index = props["menu_index"]
    if evt.kind() == InputEvent.Tab:
        if not props["is_menu_open"]:
            render(props)
            props["is_menu_open"] = True
            # handle.lock()
        else:
            # handle.unlock()
            props["is_menu_open"] = False
            handle.reset_styles()
            handle.goto(0, 1)
            handle.set_fx(Effect.Dim)
            handle.prints("─" * 16)
            handle.set_fx(Effect.Reset)
            for i, section in enumerate(sections):
                handle.goto(0, 2 + i)
                handle.prints(" " * 16)
            handle.goto(0, 7)
            handle.prints(" " * 16)
            handle.flush()

    elif evt.kind() == InputEvent.MousePressLeft:
        (col, row) = evt.data()
        if row == 0 and 0 <= col <= 5 and not props["is_menu_open"]:
            render(props)
            props["is_menu_open"] = True
            # handle.lock()
        elif row == 0 and 0 <= col <= 5 and props["is_menu_open"]:
            # handle.unlock()
            props["is_menu_open"] = False
            handle.reset_styles()
            handle.goto(0, 1)
            handle.set_fx(Effect.Dim)
            handle.prints("─" * 16)
            handle.set_fx(Effect.Reset)
            for i, section in enumerate(sections):
                handle.goto(0, 2 + i)
                handle.prints(" " * 16)
            handle.goto(0, 7)
            handle.prints(" " * 16)
            handle.flush()

    elif evt.kind() == InputEvent.Esc and props["is_menu_open"]:
        # handle.unlock()
        props["is_menu_open"] = False
        handle.reset_styles()
        handle.goto(0, 1)
        handle.set_fx(Effect.Dim)
        handle.prints("─" * 16)
        handle.set_fx(Effect.Reset)
        for i, section in enumerate(sections):
            handle.goto(0, 2 + i)
            handle.prints(" " * 16)
        handle.goto(0, 7)
        handle.prints(" " * 16)
        handle.flush()

    elif evt.kind() == InputEvent.Up and props["is_menu_open"]:
        handle.set_fx(Effect.Dim)
        if index == 0:
            handle.goto(0, 2)
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_fg(Color.Reset)
            handle.prints(sections[index].ljust(13))
            handle.set_fx(Effect.Dim)
            handle.prints("│")
            props["menu_index"] = 4
            index = props["menu_index"]
            handle.goto(0, 2 + 4)
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_bg(Color.White)
            handle.set_fg(Color.Black)
            handle.prints(sections[index].ljust(13))
            handle.set_styles(Color.Reset, Color.Reset, Effect.Dim)
            handle.prints("│")
            handle.flush()
        else:
            handle.goto(0, 2 + index)
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_fg(Color.Reset)
            handle.prints(sections[index].ljust(13))
            handle.set_fx(Effect.Dim)
            handle.prints("│")
            props["menu_index"] = index - 1
            index = props["menu_index"]
            handle.goto(0, 2 + index)
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_bg(Color.White)
            handle.set_fg(Color.Black)
            handle.prints(sections[index].ljust(13))
            handle.set_styles(Color.Reset, Color.Reset, Effect.Dim)
            handle.prints("│")
            handle.flush()

    elif evt.kind() == InputEvent.Down and props["is_menu_open"]:
        handle.set_fx(Effect.Dim)
        if index == 4:
            handle.goto(0, 2 + 4)
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_fg(Color.Reset)
            handle.prints(sections[index].ljust(13))
            handle.set_fx(Effect.Dim)
            handle.prints("│")
            props["menu_index"] = 0
            index = props["menu_index"]
            handle.goto(0, 2)
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_bg(Color.White)
            handle.set_fg(Color.Black)
            handle.prints(sections[index].ljust(13))
            handle.set_styles(Color.Reset, Color.Reset, Effect.Dim)
            handle.prints("│")
            handle.flush()
        else:
            handle.goto(0, 2 + index)
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_fg(Color.Reset)
            handle.prints(sections[index].ljust(13))
            handle.set_fx(Effect.Dim)
            handle.prints("│")
            props["menu_index"] = index + 1
            index = props["menu_index"]
            handle.goto(0, 2 + index)
            handle.prints("│")
            handle.set_fx(Effect.Reset)
            handle.set_fg(Color.Green)
            handle.prints("▎")
            handle.set_bg(Color.White)
            handle.set_fg(Color.Black)
            handle.prints(sections[index].ljust(13))
            handle.set_styles(Color.Reset, Color.Reset, Effect.Dim)
            handle.prints("│")
            handle.flush()

    elif evt.kind() == InputEvent.Enter and props["is_menu_open"]:
        # handle.unlock()
        props["is_menu_open"] = False
        props["section_id"] = index

    else:
        pass
