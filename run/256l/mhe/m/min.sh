#! /bin/bash

mdin="min.in"
mdout="min.out"
prmtop="256l.prmtop"
inpcrd="256l.rst7"
restrt="m256l.rst7"
refc="256l.rst7"
mdcrd="m256l.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
