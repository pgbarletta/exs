#! /bin/bash

mdin="min.in"
mdout="min.out"
prmtop="1xkk.prmtop"
inpcrd="1xkk.rst7"
restrt="m1xkk.rst7"
refc="1xkk.rst7"
mdcrd="m1xkk.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
