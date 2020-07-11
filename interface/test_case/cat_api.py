from cffi import FFI
import os


def build():
    ffi = FFI()

    with open("libcat.h") as header:
        func_prototypes = header.read().strip()
        ffi.cdef(func_prototypes)

    # os.environ["LD_LIBRARY_PATH"] = os.getcwd()
    ffi.set_source(
        "cat_ffi",
        '#include "libcat.h"',
        libraries=["cat"],
        # extra_link_args=['-Wl,-rpath=.', '-L$PWD']
    )

    lib = ffi.compile(verbose=True)

    return lib, ffi
