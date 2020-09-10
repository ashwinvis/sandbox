#!/bin/bash

function error_quit {
    echo -e "$@"
    echo
    echo -e 'Usage:'
    echo -e './compile.sh --clean'
    echo -e '   To clean build directory. Makenek will ask for cleaning 3rd-party libraries.'
    echo
    echo -e './compile.sh --all'
    echo -e '   To compile the code.'
    exit 1
}

#parameters
export CASE="phill"
export NEK_SOURCE_ROOT=${NEK_SOURCE_ROOT:"../../Nek5000"}

export MPI=0
if [ $MPI -eq 0 ]; then
  export FC=gfortran
  export CC=gcc
else
  export FC="mpif77"
  export CC="mpicc"
fi
export UNDERSCORE=0
export CFLAGS="-fPIC -march=native"
export FFLAGS="-fPIC -march=native -mcmodel=medium -std=legacy -Itoolbox"

export PPLIST=""
export USR="frame.o mntrlog_block.o mntrlog.o mntrtmr_block.o mntrtmr.o rprm_block.o rprm.o io_tools_block.o io_tools.o chkpoint.o chkpt_mstp.o map2D.o stat.o stat_IO.o math_tools.o"
export USR_LFLAGS=""

# arguments
args=("$@")
argsnr=$#

# check arguments
# parameters number check
if [ $[argsnr] -ne 1 ]; then
    error_quit 'Wrong arguments number!'
fi

for il in "$@"
do
case $il in
    --clean)
        ${NEK_SOURCE_ROOT}/bin/makenek clean
        shift
        ;;
    --all)
        ${NEK_SOURCE_ROOT}/bin/makenek ${CASE}
        shift
        ;;
    *)
        error_quit 'Wrong argument.'
        ;;
esac
done
