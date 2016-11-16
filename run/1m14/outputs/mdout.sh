#!/bin/bash

# Extract heat and p1m14il mdout info
perl process_mdout.perl 1p1m14.out 2p1m14.out 3p1m14.out 4p1m14.out 5p1m14.out 6p1m14.out 7p1m14.out 8p1m14.out 9p1m14.out 10p1m14.out 11p1m14.out 12p1m14.out 13p1m14.out 14p1m14.out 15p1m14.out 16p1m14.out 17p1m14.out 18p1m14.out 19p1m14.out 20p1m14.out 21p1m14.out 22p1m14.out 23p1m14.out 24p1m14.out 25p1m14.out 26p1m14.out

mv summary.ETOT etot.dat
mv summary.EPTOT eptot.dat
mv summary.EKTOT ektot.dat
mv summary.TEMP temp.dat
mv summary.PRES pres.dat
mv summary.VOLUME vol.dat
mv summary.DENSITY density.dat

rm summary*

