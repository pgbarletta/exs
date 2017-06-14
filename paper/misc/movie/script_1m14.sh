#! /bin/bash

./pava.jl -p cut_avg_1m14.pdb -v gdte_cart_1m14 -t 10 -r 0.1 -o as
ls *as.pdb | sort -n | xargs -i cat {} > 1m14_movie.pdb
sed -i 's/END/ENDMDL\nMODEL /g' 1m14_movie.pdb 
rm *as.pdb

# convert -delay 2 -loop 0 m*.png movie_1m14.gif
