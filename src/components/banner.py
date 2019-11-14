from ffi import Color, Effect

# NOTE: Issues with reseting styles on Windows
# Specifically with git-bash / winpty (and possibly
# legacy mode)


def render(props):
    handle = props["handle"]
    w = props["width"]
    # Top Bar
    handle.goto(0, 0)
    handle.set_fg(Color.Green)
    handle.prints(" ≡ ")
    handle.set_fg(Color.Reset)
    handle.prints("MENU")
    handle.goto(w - 4, 0)
    handle.set_fg(Color.Red)
    handle.prints("[x]")
    handle.set_fg(Color.Reset)
    # Horiz Rule
    handle.goto(0, 1)
    handle.set_fx(Effect.Dim)
    handle.prints("─" * w)
    handle.set_fx(Effect.Reset)
