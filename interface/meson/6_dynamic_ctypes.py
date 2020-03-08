import ctypes


class Mycom(ctypes.Structure):
    _fields_ = [("n", ctypes.c_int)]


mylib = ctypes.CDLL("./build/libdynamic.so")

mycom = Mycom.in_dll(mylib, "mycom")

print(" python> modifying /mycom/ n to 777")

mycom.n = 777

fortsub = mylib.hello
fortsub()
