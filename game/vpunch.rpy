transform start_vpunch_effect(t=1.0):
    parallel:
        align(0.5, 0.5)
        ease t/2 yoffset-15 # vertical move
        block:
            ease t yoffset +15
            ease t yoffset -15
            repeat
    parallel:
        ease t xoffset-15 # horizontal move
        block:
            ease t*2 xoffset +15
            ease t*2 xoffset -15
            repeat

transform stop_vpunch_effect():
    align(0.5, 0.5) zoom 1.0
    block:
        ease 0.5 zoom 1.005
        ease 0.5 zoom 1.0
        repeat 3