#!/home/german/julia4/bin/julia
###############################################################################
# utility to displace a PDB along a vector, generating several PDBs
###############################################################################
#   code by pgbarletta
#########################################################
# Safety pig included:
#
#    _._ _..._ .-',     _.._(`))
#   '-. `     '  /-._.-'    ',/
#      )         \            '.
#     / _    _    |             \
#    |  a    a    /              |
#    \   .-.                     ;
#     '-('' ).-'       ,'       ;
#        '-;           |      .'
#           \           \    /
#           | 7  .__  _.-\   \
#           | |  |  ``/  /`  /
#          /,_|  |   /,_/   /
#             /,_/      '`-'
###############################################################################
using DataFrames
using MIToS.PDB
using Distributions
using ArgParse
##########
# functions
##########
function read_ptraj_modes(file, modes_elements, norma::Bool=true)
    modes_file=open(file, "r")
    modes_text = readdlm(modes_file, skipstart=0, skipblanks=true,
    ignore_invalid_chars=true, comments=true, comment_char='\*')
    close(modes_file)

    nmodes = modes_text[1, 5]
    ncoords = convert(Int64, modes_elements)
    lines = ceil(Int64, ncoords/7)
    rest = convert(Int64, ncoords % 7)

    eval=Array{Float64}(nmodes);
    mode = Array{Float64}(ncoords, nmodes);
    temp1=Array{Float64}(ncoords, 1);
    temp2 = Array{Float64}(ncoords+(7-rest));

    j=lines + 1 + 2 # 1 p/ q lea la prox linea 2 por el header

    for i=1:nmodes
        eval[i] = modes_text[j, 2]
        temp = transpose(modes_text[(j+1):(lines+j), :])
        temp2 = reshape(temp, ncoords+(7-rest))
        for k=(rest+1):7
            pop!(temp2)
        end
    mode[:, i] = temp2
        j = j + lines + 1
    end

    if norma == true
        for i=1:nmodes
            mode[: ,i] = mode[:, i] / norm(mode[:, i])
        end
    end

    return mode, eval
end
#########
function displaceAA(mod_pdb, vector1, multiplier)
  # Preparo variables
    pdb = copy(mod_pdb)
    struct_xyz = coordinatesmatrix(pdb)
    new_struct_xyz = copy(struct_xyz)
    natom = Array{Int64}(1)
    vector = Array{Float64}(1, 3)
   aa = length(pdb)
   # Determino el nro de atomos de c/ aminoácido
   for i=1:aa
       push!(natom, length(pdb[i]))
   end
   shift!(natom)
   temp1 = Array{Int64}(natom[1],3)

   # Adapto el vector p/ darle la misma forma q la matriz de coordenadas
    for i=1:3:length(vector1)
        if i== 1
            vector = reshape(vector1[i:i+2], 1, 3)
            continue
        end
        vector = vcat(vector, reshape(vector1[i:i+2], 1, 3))
    end

   for i=1:aa
       if i == 1
           temp1 = repmat(vector[i, :], natom[i], 1)
           continue
       end
       temp2 = repmat(vector[i, :], natom[i], 1)
       temp1 = vcat(temp1, temp2)
   end
   sum_mat = temp1

   # Listo, ahora puedo mover el pdb
   new_struct_xyz  = struct_xyz + sum_mat .* multiplier
   pdb = change_coordinates(pdb, new_struct_xyz);
   return pdb
end
#########
function displaceAtoms(mod_pdb, vector1, multiplier)
  # Preparo variables
    pdb = copy(mod_pdb)
    struct_xyz = coordinatesmatrix(pdb)
#    new_struct_xyz = copy(struct_xyz)
    vector = Array{Float64}(1, 3)

    # Adapto el vector p/ darle la misma forma q la matriz de coordenadas
    for i=1:3:length(vector1)
        if i== 1
            vector = reshape(vector1[i:i+2], 1, 3)
            continue
        end
        vector = vcat(vector, reshape(vector1[i:i+2], 1, 3))
    end

    # Listo, ahora puedo mover el pdb
    new_struct_xyz  = struct_xyz + vector .* multiplier
    pdb = change_coordinates(pdb, new_struct_xyz);
   return pdb
end
#########
# Arg Parse settings
s = ArgParseSettings()
@add_arg_table s begin
    "--inpdb", "-p"
        help = "Input PDB"
        arg_type = ASCIIString
        required = true
    "--vector", "-v"
        help = "Input vector"
        arg_type = ASCIIString
        required = true
    "--top", "-t"
        help = "Top/bottom multiplier"
        arg_type = Int
        required = true
    "--resolution", "-r"
        help = "Step size between output structures. Along with --top parameter
determines the number of output structures "
        arg_type = Float64
        required = true
    "--outpdb", "-o"
        help = "Output PDBs prefix"
        arg_type = ASCIIString
        required = true
    "--index", "-i"
        help = "Mode number when reading cpptraj PCA modes"
        arg_type = Int
        default = 0
    "--script"
        help = "Only write output PDB"
        action = :store_true
end

##########
# main program
##########

# Read arguments from console
parsed_args = parse_args(ARGS, s)
args = Array{Any, 1}(0)
for (arg, val) in parsed_args
    arg=symbol(arg)
    @eval (($arg) = ($val))
end
# Append ".pdb" to output pdb
outpdb = outpdb * ".pdb"

println("Input parameters:")
println("INPDB          ", inpdb)
println("VECTOR         ", vector)
println("TOP            ", top)
println("RESOLUTION     ", resolution)
println("OUTPDB         ", outpdb)
println("INDEX          ", parsed_args["index"])
println("script?        ", script)

# Get ready
in_vec = Array{Float64, 1}

# Read PDB
in_pdb = read(string(inpdb), PDBFile, group="ATOM");
nres_xyz = 3*length(in_pdb)
natom_xyz = size(coordinatesmatrix(in_pdb))[1] * 3

if parsed_args["index"] != 0
# Vector de PCA Amber
    try
        in_vec = read_ptraj_modes(vector, nres_xyz, true)[1][:, index]
    catch
        try
            in_vec = read_ptraj_modes(vector, natom_xyz, true)[1][:, index]
        end
    end
else
# Vector puro
    in_vec = convert(Array{Float64}, readtable(vector)[:, 1]);
end

# In case input vector file is note found
if in_vec == Array{Float64, 1}
    throw(ArgumentError(string("\n\n", vector, message_vec_not_found)))
end

# Check --top argument is actually bigger than step size
if top <= resolution
    throw(ArgumentError(string("\n\n --top argument ", top," is smaller/equal
than --resolution argument ", resolution)))
end

# Ahora desplazo
cnt = 0
if nres_xyz == length(in_vec)
# El modo es de Calpha
    in_vec = in_vec / norm(in_vec)
    for step in -top:resolution:top
        out_pdb = displaceAA(in_pdb, in_vec, step);
        # Y guardo
        cnt+=1
        out_filename = string(cnt, "_", outpdb)
        write(out_filename, out_pdb, PDBFile)
    end
 
elseif natom_xyz == length(in_vec)
# El modo es all-atom
    in_vec = in_vec / norm(in_vec)

    for step in -top:resolution:top
        out_pdb = displaceAtoms(in_pdb, in_vec, step);
        # Y guardo
        cnt+=1
        out_filename = string(cnt, "_", outpdb)
        write(out_filename, out_pdb, PDBFile)
    end

else
# El modo no tiene el tamaño adecuado
error("PDB and input vector don't match.\nPDB has ", length(in_pdb) ,
" amino acids and ", size(coordinatesmatrix(in_pdb))[1] * 3, " atoms.\nVector has ",
length(in_vec), " elements, which should correspond to ", length(in_vec) / 3, " particles.")
end


# Finalmente, hago el script
#if script == true
#    load = "cmd.load(\""
#    f = open("script_porky.py", "w")
#    write(f, "from pymol.cgo import *\n")
#    write(f, "from pymol import cmd\n\n")
#    write(f, load, inpdb,"\")\n")
#    write(f, load, outpdb,"\")\n")
#    write(f, load,"modevectors.py\")\n")
#    write(f, "modevectors(\"", inpdb[1:end-4], "\", \"", outpdb[1:end-4], "\", ")
#    write(f, "outname=\"modevectors\", head=1.0, tail=0.3, headrgb = \"1.0, 1.0, 0.0\", tailrgb = \"1.0, 1.0, 0.0\") ")
#    close(f)
#end
