#! /bin/bash

./pava.jl -p avg_1hvr_hol.pdb -v gdte_cart_1hvr_hol -t 10 -r 0.1 -o as
ls *as.pdb | sort -n | xargs -i cat {} > 1hvr_hol_movie.pdb
sed -i 's/END/ENDMDL\nMODEL /g' 1hvr_hol_movie.pdb 
rm *as.pdb

# convert -delay 2 -loop 0 hol*.png movie_1hvr_hol.gif
