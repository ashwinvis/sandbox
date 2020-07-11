import os

def setup():
    os.system('make libcat.so')


def teardown():
    os.system('make clean')
    pass


def pet_cat(mode, lib):
    print("Initializing cat", mode)
    lib.init_cat()

    if mode == "ABI":
        # FIXME: it does not work in API mode
        # FIXME: arguments are not passed into Fortran
        print("cset_meow")
        lib.cset_meow(24.0)

        print("set_meow")
        lib.set_meow(8.0)

    print("get_cat")
    cat = lib.get_cat()
    print("Python says cat =", cat)


def test_abi():
    from cat_abi import load

    lib, ffi = load()
    pet_cat("ABI", lib)


def test_api():
    from cat_api import build

    lib, ffi = build()

    import cat_ffi

    pet_cat("API", cat_ffi.lib)
