#!/usr/bin/env python

import time

import pycozmo


def pycozmo_program(cli: pycozmo.client.Client):

    # Load animations - one time.
    cli.load_anims()

    # Print the names of all available animations.
    names = cli.get_anim_names()
    for name in sorted(names):
        print(name)

    time.sleep(2)

    # Play an animation.
    cli.play_anim("anim_launch_wakeup_01")
    cli.wait_for(pycozmo.event.EvtAnimationCompleted)


pycozmo.run_program(pycozmo_program)
