#! /bin/bash

export CUDA_VISIBLE_DEVICES="0"

mdin="hea.in"
mdout="hea.out"
prmtop="1prn.prmtop"
inpcrd="mm1prn.rst7"
restrt="h1prn.rst7"
refc="mm1prn.rst7"
mdcrd="h1prn.nc"

pmemd.cuda -O -i $mdin -o $mdout -p $prmtop -c $inpcrd -r $restrt -ref $refc -x $mdcrd 

exit 0
