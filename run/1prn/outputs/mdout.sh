#!/bin/bash

# Extract heat and p1prnil mdout info
perl process_mdout.perl 1p1prn.out 2p1prn.out 3p1prn.out 4p1prn.out 5p1prn.out 6p1prn.out 7p1prn.out 8p1prn.out 9p1prn.out 10p1prn.out 11p1prn.out 12p1prn.out 13p1prn.out 14p1prn.out 15p1prn.out 16p1prn.out 17p1prn.out 18p1prn.out 19p1prn.out 20p1prn.out 21p1prn.out 22p1prn.out 23p1prn.out 24p1prn.out 25p1prn.out 

mv summary.ETOT etot.dat
mv summary.EPTOT eptot.dat
mv summary.EKTOT ektot.dat
mv summary.TEMP temp.dat
mv summary.PRES pres.dat
mv summary.VOLUME vol.dat
mv summary.DENSITY density.dat

rm summary*

