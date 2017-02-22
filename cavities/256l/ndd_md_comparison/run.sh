#! /bin/bash

cpptraj < nc-to-pdb_cpp_in > nc-to-pdb_cpp_out

ls *frame* | sort -V > temp
cat temp | xargs -i mv {} {}.pdb
rm temp
ls *frame* | sort -V > in_ndd

time ANA cut_avg_256l.pdb -c 1_256l.cfg --NDD_input in_ndd --NDD_output out_ndd

exit 0
