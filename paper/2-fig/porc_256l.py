from pymol import cmd

cmd.load("./cut_avg_256l.pdb")

cmd.set_view ( '''0.315200627,   -0.223496795,    0.922329843,\
     0.930618227,    0.263243794,   -0.254244953,\
    -0.185979143,    0.938482106,    0.290963858,\
    -0.000527410,   -0.000355184, -100.719245911,\
    32.342666626,   35.357192993,   38.785629272,\
  -274.016784668,  475.400878906,  -20.000000000''' )


cmd.hide("lines")
cmd.show("cartoon")
cmd.color("skyblue", "cut_avg_256l")
cmd.set("cartoon_fancy_helices", 1)
cmd.set("ray_trace_mode",  1)
cmd.set("two_sided_lighting", "on")
cmd.set("reflect", 0)
cmd.set("ambient", 0.5)
cmd.set("ray_trace_mode",  0)
cmd.set('''ray_opaque_background''', '''off''')


cmd.png("2d--fig_256l.png", width=1800, height=1100, dpi=600, ray=1)
