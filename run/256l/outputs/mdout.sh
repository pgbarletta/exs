#!/bin/bash

# Extract heat and p256lil mdout info
perl process_mdout.perl 1p256l.out 2p256l.out 3p256l.out 4p256l.out 5p256l.out 6p256l.out 7p256l.out 8p256l.out 9p256l.out 10p256l.out 11p256l.out 12p256l.out 13p256l.out 14p256l.out 15p256l.out 16p256l.out 17p256l.out 18p256l.out 19p256l.out 20p256l.out 21p256l.out 22p256l.out 23p256l.out 24p256l.out 25p256l.out 26p256l.out 27p256l.out 28p256l.out 29p256l.out 30p256l.out

mv summary.ETOT etot.dat
mv summary.EPTOT eptot.dat
mv summary.EKTOT ektot.dat
mv summary.TEMP temp.dat
mv summary.PRES pres.dat
mv summary.VOLUME vol.dat
mv summary.DENSITY density.dat

rm summary*

