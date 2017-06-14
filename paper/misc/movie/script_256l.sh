#! /bin/bash

./pava.jl -p cut_avg_256l.pdb -v gdte_cart_256l -t 10 -r 0.1 -o as
ls *as.pdb | sort -n | xargs -i cat {} > 256l_movie.pdb
sed -i 's/END/ENDMDL\nMODEL /g' 256l_movie.pdb 
rm *as.pdb
