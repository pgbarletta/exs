#! /bin/bash

mdin="mmin.in"
mdout="mmin.out"
prmtop="1hvr_apo.prmtop"
inpcrd="m1hvr_apo.rst7"
restrt="mm1hvr_apo.rst7"
refc="1hvr_apo.rst7"
mdcrd="mm1hvr_apo.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
