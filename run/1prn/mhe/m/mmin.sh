#! /bin/bash

mdin="mmin.in"
mdout="mmin.out"
prmtop="1prn.prmtop"
inpcrd="m1prn.rst7"
restrt="mm1prn.rst7"
refc="1prn.rst7"
mdcrd="mm1prn.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
