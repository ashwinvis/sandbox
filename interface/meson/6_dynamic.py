from cffi import FFI


ffi = FFI()

ffi.cdef("void hello();")

lib = ffi.dlopen("build/libdynamic.so")

lib.hello()
