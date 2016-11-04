#! /bin/bash

mdin="min.in"
mdout="min.out"
prmtop="1prn.prmtop"
inpcrd="1prn.rst7"
restrt="m1prn.rst7"
refc="1prn.rst7"
mdcrd="m1prn.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
