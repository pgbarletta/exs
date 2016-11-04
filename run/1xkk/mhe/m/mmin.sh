#! /bin/bash

mdin="mmin.in"
mdout="mmin.out"
prmtop="1xkk.prmtop"
inpcrd="m1xkk.rst7"
restrt="mm1xkk.rst7"
refc="1xkk.rst7"
mdcrd="mm1xkk.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
