#! /bin/bash

export CUDA_VISIBLE_DEVICES="1"

mdin="hea.in"
mdout="hea.out"
prmtop="1hvr_hol.prmtop"
inpcrd="mm1hvr_hol.rst7"
restrt="h1hvr_hol.rst7"
refc="mm1hvr_hol.rst7"
mdcrd="h1hvr_hol.nc"

pmemd.cuda -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
