#!/bin/bash

# Extract heat and equil mdout info
perl process_mdout.perl 1p1hvr_hol.out 2p1hvr_hol.out 3p1hvr_hol.out 4p1hvr_hol.out 5p1hvr_hol.out 6p1hvr_hol.out 7p1hvr_hol.out 8p1hvr_hol.out 9p1hvr_hol.out 10p1hvr_hol.out 11p1hvr_hol.out 12p1hvr_hol.out 13p1hvr_hol.out 14p1hvr_hol.out 15p1hvr_hol.out 16p1hvr_hol.out 17p1hvr_hol.out 18p1hvr_hol.out 19p1hvr_hol.out 20p1hvr_hol.out 21p1hvr_hol.out 22p1hvr_hol.out 23p1hvr_hol.out 24p1hvr_hol.out 25p1hvr_hol.out 26p1hvr_hol.out 27p1hvr_hol.out 


mv summary.ETOT etot.dat
mv summary.EPTOT eptot.dat
mv summary.EKTOT ektot.dat
mv summary.TEMP temp.dat
mv summary.PRES pres.dat
mv summary.VOLUME vol.dat
mv summary.DENSITY density.dat

rm summary*

