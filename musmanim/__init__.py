from manim import *
from .animations import *
from .note_shapes import *
from .text import *  # important that it is after manim, for Text override.



def to_nl(nl_num, nl: NumberLine,
          *, buff=UP*0.2 + RIGHT*0.1) -> np.ndarray:
    return nl.number_to_point(nl_num) + buff


ADD_SOUND = False


def play_rhythm(scene, group, timings, max_wiggle_time=1.0, add_sound=ADD_SOUND):
    '''
    Only add sound when rendering the whole file otherwise, you cannot
    create partial files
    '''
    if len(group) != len(timings):
        raise ValueError('Group length must equal timing length')
    for i, obj in enumerate(group):
        timing = timings[i]
        wiggle_time = min(max_wiggle_time, timing)
        if add_sound:
            scene.add_sound('assets/sounds/basic_pluck.wav', time_offset=0.2)
            # a little slow.
        scene.play(Wiggle(obj), run_time=wiggle_time)
        if timing > max_wiggle_time:
            scene.wait(timing - max_wiggle_time)




