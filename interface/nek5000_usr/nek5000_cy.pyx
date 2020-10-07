# cython: language_level=3

from mpi4py import MPI
#  comm = MPI.COMM_WORLD
#  nb_proc = comm.size
#  rank = comm.Get_rank()
#

from mpi4py cimport MPI
from mpi4py.libmpi cimport *


cdef extern from "libnek5000.h":
    void nek_init_(int* comm)


cpdef nek_init_cy():
    cdef MPI.Comm comm = MPI.COMM_WORLD
    nek_init_(<int*>comm.ob_mpi)

