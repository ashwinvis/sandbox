import os
import numpy as np


def setup():
    os.system('make libcat.so')
    from cat_api import build

    lib, ffi = build()


def teardown():
    # os.system('make clean')
    pass


def asarray( ffi, ptr, length ):
    """https://bitbucket.org/cffi/cffi/issues/292/cant-copy-data-to-a-numpy-array
    https://gist.github.com/yig/77667e676163bbfc6c44af02657618a6
    """
    ## Get the canonical C type of the elements of ptr as a string.
    T = ffi.getctype( ffi.typeof( ptr ).item )
    # print( T )
    # print( ffi.sizeof( T ) )

    #  if T not in ctype2dtype:
    #      raise RuntimeError( "Cannot create an array for element type: %s" % T )

    return np.frombuffer(ffi.buffer(ptr, length*ffi.sizeof(T)), np.dtype('f8'))

def pet_cat(mode, lib, ffi):
    print("Initializing cat", mode)
    lib.init_cat()

    # https://stackoverflow.com/a/16290289
    float_array = np.eye(3) * 33
    float_ptr = ffi.cast("double *", float_array.ctypes.data)

    print("cset_meow")
    lib.cset_meow(float_ptr)

    print("set_meow")
    lib.set_meow(float_ptr)

    print("get_cat")
    #  cat = np.empty((3, 3), dtype=np.float64)
    #  print("Python says cat =", cat)
    cat_ptr = ffi.new("double *")
    lib.get_cat(cat_ptr)

    cat = asarray(ffi, cat_ptr, 9)
    # FIXME: does not return the correct values
    print("Python says cat =", cat)


def test_abi():
    from cat_abi import load

    lib, ffi = load()
    pet_cat("ABI", lib, ffi)


def test_api():
    import cat_ffi

    pet_cat("API", cat_ffi.lib, cat_ffi.ffi)
