#! /bin/bash

export CUDA_VISIBLE_DEVICES="0"

mdin="hea.in"
mdout="hea.out"
prmtop="1hvr_apo.prmtop"
inpcrd="mm1hvr_apo.rst7"
restrt="h1hvr_apo.rst7"
refc="mm1hvr_apo.rst7"
mdcrd="h1hvr_apo.nc"

pmemd.cuda -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
