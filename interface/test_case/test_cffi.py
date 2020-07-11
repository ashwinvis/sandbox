import os

def setup():
    os.system('make libcat.so')
    from cat_api import build

    lib, ffi = build()


def teardown():
    os.system('make clean')
    pass


def pet_cat(mode, lib, ffi):
    print("Initializing cat", mode)
    lib.init_cat()

    # FIXME: If API mode is used it cannot be run in the same process which
    #        builds it? Leads to segfault. OK if imported later
    #
    # FIXME: arguments are not passed into Fortran

    float_ptr = ffi.new("double *", 24.0)

    print("cset_meow")
    lib.cset_meow(float_ptr)

    print("set_meow")
    lib.set_meow(float_ptr)

    print("get_cat")
    cat = lib.get_cat()
    print("Python says cat =", cat)


def test_abi():
    from cat_abi import load

    lib, ffi = load()
    pet_cat("ABI", lib, ffi)


def test_api():
    import cat_ffi

    pet_cat("API", cat_ffi.lib, cat_ffi.ffi)
