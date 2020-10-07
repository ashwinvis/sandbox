from cffi import FFI


def build():
    ffi = FFI()

    for file in ["libnek5000.h"]:
        with open(file) as header:
            func_prototypes = header.read()
            ffi.cdef(func_prototypes)

    MPI = False

    # os.environ["LD_LIBRARY_PATH"] = os.getcwd()

    source = """
#include "libnek5000.h"
"""
    if MPI:
        #  source = '#include "mpi.h"' + source
        ffi.cdef("#define MPI_COMM_WORLD ...")

    # import subprocess
    # ompi_ldflags = subprocess.getoutput("pkg-config --libs ompi").split()
    #  extra_link_args=ompi_ldflags
    # ['-Wl,-rpath=.', '-L$PWD']
    if MPI:
        ffi.set_source_pkgconfig(
            "nek5000_ffi",
            pkgconfig_libs=["ompi"],
            source=source,
            libraries=["nek5000"],
        )
    else:
        ffi.set_source(
            "nek5000_ffi",
            source=source,
            libraries=["nek5000"],
        )

    lib = ffi.compile(verbose=True)

    return lib, ffi


if __name__ == "__main__":
    build()
