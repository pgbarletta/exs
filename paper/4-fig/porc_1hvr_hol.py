from pymol import cmd

cmd.load("modevectors.py")
cmd.load("./avg_1hvr_hol.pdb")
cmd.load("disp_avg_1hvr_hol.pdb")

cmd.set_view ( '''-0.554374218,    0.354257464,    0.753099322,\
    -0.799625099,    0.024184536,   -0.599998593,\
    -0.230775893,   -0.934826553,    0.269876897,\
     0.000570767,   -0.000263005, -126.341300964,\
    44.034534454,   42.536033630,   34.025039673,\
   -99.837615967,  352.591064453,  -20.000000000''' )


modevectors("avg_1hvr_hol", "disp_avg_1hvr_hol", head=.7, tail=0.2, head_length=1.2, headrgb=".25,.5,.8", tailrgb=".25,.5,.8", cutoff=1.5)

cmd.set('''ray_opaque_background''', '''off''')

cmd.png("4b-porc_1hvr_hol.png", width=3600, height=2300, dpi=600, ray=1)
