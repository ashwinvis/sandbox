import nek5000_cy
#  from nek5000_ffi import lib, ffi

# from fluiddyn.util.mpi import comm, rank, nb_proc


# _comm = ffi.new("MPI_Comm *")
# print(comm, dir(comm), _comm)
#  _rank = ffi.new("int*")
#  _comm.rank = _rank
#  _size = ffi.new("int *")
#  _comm.size = _size

nek5000_cy.nek_init_cy()

#  dummy_comm = ffi.cast('int', 0)
#  print("dummy_comm", dummy_comm)
#  lib.nek_init_(dummy_comm)

#lib.nek_solve_()
#lib.nek_end_()
