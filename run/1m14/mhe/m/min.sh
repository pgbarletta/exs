#! /bin/bash

mdin="min.in"
mdout="min.out"
prmtop="1m14.prmtop"
inpcrd="1m14.rst7"
restrt="m1m14.rst7"
refc="1m14.rst7"
mdcrd="m1m14.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
