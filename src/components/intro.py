from ffi import Effect


def render(props):
    handle = props["handle"]
    offset = props["offset_mid"]
    (w, h) = (props["width"], props["height"])
    # Intro
    from_top = h // 3
    # Print Title
    title = "Dave Ho CLI v0.beta"
    from_col = w // 2 - (len(title) // 2) - offset
    handle.goto(from_col, from_top)
    handle.prints(title)
    # Print Subtitle
    subtitle = "\\\'dæv • \'hoh\\  賀毅超  (he, him, his)"
    from_col = w // 2 - (len(subtitle) + 3) // 2 - offset
    handle.goto(from_col, from_top + 1)
    handle.prints(subtitle[:13])
    handle.set_fx(Effect.Dim)
    handle.prints(subtitle[13:20])
    handle.set_fx(Effect.Reset)
    handle.prints(subtitle[20:])