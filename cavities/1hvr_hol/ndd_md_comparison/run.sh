#! /bin/bash

cpptraj < nc-to-pdb_cpp_in > nc-to-pdb_cpp_out

ls *frame* | sort -V > temp
cat temp | xargs -i mv {} {}.pdb
rm temp
ls *frame* | sort -V > in_ndd

time ANA apoavg_1hvr_hol.pdb -c 2_1hvr_hol.cfg --NDD_input in_ndd --NDD_output out_ndd

exit 0
