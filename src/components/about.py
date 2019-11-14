import asyncio
from os import path
from random import shuffle
from webbrowser import open_new_tab
from ffi import Clear, InputEvent


async def render(props):
    tty = props["dispatcher"]
    w = props["size"][0]
    # Setup messages
    quotes = [
        ("Find the good", "and believe it"),
        ("Perfect is the", "enemy of great"),
        ("Thru discipline", "comes freedom"),
        ("if knocked_down:", "  get_up += 1"),
        ("Non nobis solum", "nati sumus"),
        ("Ad astra", "per aspera")]
    errors = [
        ("404 Not Found:", "file `good.py`"),
        ("ERR04 Recursion", "depth exceeded"),
        ("[error]: cannot", "assign to field"),
        ("[!] `undefined`", "is not an object"),
        ("RefErr: event", "is undefined"),
        ("#: Cannot find", "vcvarsall.bat")]
    relaxes = [
        ("Ok, keep calm", "and carry on"),
        ("Hmm...oh! Just", "a typo : vs ;"), 
        ("www.reddit.com/", "r/funnycats"),
        ("It works again!", "...no idea why"),
        ("Not a bug! Call", "it a feature!"),
        ("Maybe it's time", "to recaffinate!")]
    indices = [0, 1, 2, 3, 4, 5]
    shuffle(indices)
    scene_delay = 0.1
    # Read animation file
    scenes_path = path.join(path.abspath(
        path.dirname(path.abspath(__file__))),
        "scenes.txt")
    scene_len = 0
    scene_queue = asyncio.Queue(maxsize=263)
    with open(scenes_path, encoding="utf-8", mode="r") as f:
        scenes = f.read().split('1.')
        for scene in scenes:
            scene_len += 1
            try:
                scene_queue.put_nowait(scene)
            except asyncio.QueueFull:
                raise("Incorrect scene length")
    # <-- close file

    # Setup screen
    tty.clear(Clear.CursorDown)
    (start_col, start_row) = (0, 3)
    (iterations, full_loops) = (0, 0)
    (msg_ax, msg_bx) = (102, 175)
    tty.goto(start_col, start_row)
    msg_id = indices.pop()
    while True:
        if props["section_id"] != 0 or not props["is_running"]:
            break
        tty.goto(start_col, start_row)
        tty.clear(Clear.CursorDown)
        scene = await scene_queue.get()
        # put scene back to make circular buffer
        await scene_queue.put(scene)
        if (iterations % scene_len) in range(46, 73):
            (qav, qbv) = quotes[msg_id]
            (end_ax, end_bx) = (msg_ax + len(qav), msg_bx + len(qbv))
            msg = scene[3:msg_ax] + qav + \
                scene[end_ax:msg_bx] + qbv + scene[end_bx:]
        elif (iterations % scene_len) in range(74, 99):
            (eav, ebv) = errors[msg_id]
            (end_ax, end_bx) = (msg_ax + len(eav), msg_bx + len(ebv))
            msg = scene[3:msg_ax] + eav + \
                scene[end_ax:msg_bx] + ebv + scene[end_bx:]
        elif (iterations % scene_len) in range(120, 132):
            (rav, rbv) = relaxes[msg_id]
            (end_ax, end_bx) = (msg_ax + len(rav), msg_bx + len(rbv))
            msg = scene[3:msg_ax] + rav + \
                scene[end_ax:msg_bx] + rbv + scene[end_bx:]
        elif iterations == scene_len:
            iterations = 1
            full_loops += scene_len
            try:
                msg_id = indices.pop()
            except IndexError:
                indices.extend([0, 1, 2, 3, 4, 5])
                shuffle(indices)
                msg_id = indices.pop()
            await asyncio.sleep(scene_delay)
            continue
        else:
            msg = scene[3:]
        iterations += 1
        tty.printf(msg)
        await asyncio.sleep(scene_delay)
    # <-- end loop


async def handle(props):
    delay = props["delay"]
    tty = props["dispatcher"]
    with tty.spawn() as handle:
        while True:
            await asyncio.sleep(delay)
            evt = handle.poll_latest_async()
            if evt is None:
                continue
            if not props["is_running"] or props["section_id"] != 0:
                break
            # TODO: example case, replace with click events
            if evt.kind() == InputEvent.Char:
                if evt.data() == 'g':
                    open_new_tab("https://github.com/imdaveho")
                    break
        # <-- end loop
    # <-- close handle