from cffi import FFI


def load():
    ffi = FFI()

    with open("libcat.h") as header:
        ffi.cdef(header.read().strip())

    lib = ffi.dlopen("libcat.so")
    return lib, ffi
