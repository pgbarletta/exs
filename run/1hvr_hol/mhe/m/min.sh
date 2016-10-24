#! /bin/bash

mdin="min.in"
mdout="min.out"
prmtop="1hvr_hol.prmtop"
inpcrd="1hvr_hol.rst7"
restrt="m1hvr_hol.rst7"
refc="1hvr_hol.rst7"
mdcrd="m1hvr_hol.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
