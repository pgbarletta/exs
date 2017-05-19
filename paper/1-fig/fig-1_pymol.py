from pymol import cmd

cmd.load("avg_1hvr_apo.pdb")
cmd.load("out_2_avg_1hvr_apo_1.pdb")
cmd.load("out_lop_avg_1hvr_apo_1.pdb")
cmd.load("out_hip_avg_1hvr_apo_1.pdb")

cmd.set_view ( '''-0.554374218,    0.354257464,    0.753099322,\
    -0.799625099,    0.024184536,   -0.599998593,\
    -0.230775893,   -0.934826553,    0.269876897,\
     0.000570767,   -0.000263005, -126.341300964,\
    44.034534454,   42.536033630,   34.025039673,\
   -99.837615967,  352.591064453,  -20.000000000''' )


cmd.load("out_CH_1hvr_apo.py")
cmd.show("lines", "out_*_avg_1hvr_apo_1")
cmd.set('''ray_opaque_background''', '''off''')
cmd.color("skyblue", "avg_1hvr_apo")
cmd.color("deepsalmon", "out_2_avg_1hvr_apo_1")
cmd.color("red", "out_hip_avg_1hvr_apo_1")
cmd.color("red", "out_lop_avg_1hvr_apo_1")
cmd.set("cartoon_fancy_helices", 1)
cmd.set("ray_trace_mode",  1)
cmd.set("two_sided_lighting", "on")
cmd.set("reflect", 0)
cmd.set("ambient", 0.5)


#cmd.png("2a--fig_1hvr_apo.png", width=3600, height=2300, dpi=600, ray=1)
