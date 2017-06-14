#! /bin/bash

./pava.jl -p avg_1hvr_apo.pdb -v gdte_cart_1hvr_apo -t 10 -r 0.1 -o as
ls *as.pdb | sort -n | xargs -i cat {} > 1hvr_apo_movie.pdb
sed -i 's/END/ENDMDL\nMODEL /g' 1hvr_apo_movie.pdb 
rm *as.pdb

# convert -delay 2 -loop 0 apo*.png movie_1hvr_apo.gif
