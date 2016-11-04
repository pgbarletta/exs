#! /bin/bash

mdin="mmin.in"
mdout="mmin.out"
prmtop="1m14.prmtop"
inpcrd="m1m14.rst7"
restrt="mm1m14.rst7"
refc="1m14.rst7"
mdcrd="mm1m14.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
