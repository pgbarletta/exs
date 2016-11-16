#! /bin/bash

mdin="mmin.in"
mdout="mmin.out"
prmtop="256l.prmtop"
inpcrd="m256l.rst7"
restrt="mm256l.rst7"
refc="256l.rst7"
mdcrd="mm256l.crd"

pmemd -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
