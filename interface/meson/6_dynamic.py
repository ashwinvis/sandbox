from cffi import FFI


ffi = FFI()

ffi.cdef(
    """
    void hello();
    struct MyCom {
        int n;
    } mycom = {};

"""
)
#  struct MyCom mycom = {0};

#  typedef struct {
#      int n;
#  } mycom;

lib = ffi.dlopen("build/libdynamic.so")


mycom = ffi.new("struct MyCom *", [5])

print("Python mycom.n", mycom.n)
mycom.n += 1
print("Python mycom.n", mycom.n)
mycom[0] = {"n": 777}
print("Python mycom.n", mycom.n)

print("Type of Python mycom  =", type(mycom))
print("Address of Python mycom =", ffi.addressof(mycom, 0))
print("Address of hello =", ffi.addressof(lib, "hello"))
print("Address of /mycom/ =", ffi.addressof(lib, "mycom"))
print("Python modifying /mycom/ n...")
lib.mycom.n = 778
#  n = ffi.cast("int", 1)
#  mycom = ffi.new("mycom *", {"n": 1})
#  print(mycom)

lib.hello()
