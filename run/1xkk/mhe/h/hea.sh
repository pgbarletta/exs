#! /bin/bash

export CUDA_VISIBLE_DEVICES="0"

mdin="hea.in"
mdout="hea.out"
prmtop="1xkk.prmtop"
inpcrd="mm1xkk.rst7"
restrt="h1xkk.rst7"
refc="mm1xkk.rst7"
mdcrd="h1xkk.nc"

pmemd.cuda -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
