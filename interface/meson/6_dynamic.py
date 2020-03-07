from cffi import FFI


ffi = FFI()

ffi.cdef("void hello_();")

lib = ffi.dlopen("build/libdynamic.so")

lib.hello_()
