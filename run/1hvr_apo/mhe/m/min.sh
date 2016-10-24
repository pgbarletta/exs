#! /bin/bash

mdin="min.in"
mdout="min.out"
prmtop="1hvr_apo.prmtop"
inpcrd="1hvr_apo.rst7"
restrt="m1hvr_apo.rst7"
refc="1hvr_apo.rst7"
mdcrd="m1hvr_apo.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
