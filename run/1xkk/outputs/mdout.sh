#!/bin/bash

# Extract heat and p1xkkil mdout info
perl process_mdout.perl 1p1xkk.out 2p1xkk.out 3p1xkk.out 4p1xkk.out 5p1xkk.out 6p1xkk.out 7p1xkk.out 8p1xkk.out 9p1xkk.out 10p1xkk.out 11p1xkk.out 12p1xkk.out 13p1xkk.out 14p1xkk.out 15p1xkk.out 16p1xkk.out 17p1xkk.out 18p1xkk.out 19p1xkk.out 20p1xkk.out 21p1xkk.out 22p1xkk.out 23p1xkk.out 24p1xkk.out 25p1xkk.out 26p1xkk.out 27p1xkk.out 28p1xkk.out

mv summary.ETOT etot.dat
mv summary.EPTOT eptot.dat
mv summary.EKTOT ektot.dat
mv summary.TEMP temp.dat
mv summary.PRES pres.dat
mv summary.VOLUME vol.dat
mv summary.DENSITY density.dat

rm summary*

