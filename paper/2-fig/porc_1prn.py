from pymol import cmd

cmd.load("modevectors.py")
cmd.load("./avg_1prn.pdb")
cmd.load("disp_avg_1prn.pdb")

cmd.set_view ( '''0.705788314,   -0.370076984,   -0.604060292,\
    -0.475935459,    0.383867979,   -0.791268468,\
     0.524721146,    0.845966756,    0.094793379,\
    -0.000039771,   -0.000701737, -149.239501953,\
    37.312110901,   36.388977051,   37.234172821,\
   112.251243591,  186.226913452,  -20.000000000''' )

modevectors("avg_1prn", "disp_avg_1prn", head=.7, tail=0.2, head_length=1.2, headrgb=".25,.5,.8", tailrgb=".25,.5,.8", cutoff=1.5)

cmd.png("4c-porc_1prn.png", width=1800, height=1100, dpi=600, ray=1)
