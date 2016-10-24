#! /bin/bash

mdin="mmin.in"
mdout="mmin.out"
prmtop="1hvr_hol.prmtop"
inpcrd="m1hvr_hol.rst7"
restrt="mm1hvr_hol.rst7"
refc="1hvr_hol.rst7"
mdcrd="mm1hvr_hol.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
