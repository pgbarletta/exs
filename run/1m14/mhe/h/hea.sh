#! /bin/bash

export CUDA_VISIBLE_DEVICES="1"

mdin="hea.in"
mdout="hea.out"
prmtop="1m14.prmtop"
inpcrd="mm1m14.rst7"
restrt="h1m14.rst7"
refc="mm1m14.rst7"
mdcrd="h1m14.nc"

pmemd.cuda -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
