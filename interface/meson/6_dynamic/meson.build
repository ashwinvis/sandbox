project('dynamic_fortran', 'fortran', default_options : ['buildtype=release'])

fc = meson.get_compiler('fortran')
fcid = fc.get_id()

if fcid == 'intel-cl' or (host_machine.system() == 'windows' and fcid == 'pgi')
  error('MESON_SKIP_TEST: non-Gfortran Windows Fortran compilers do not do shared libraries in a Fortran standard way')
  # !DEC$ ATTRIBUTES DLLEXPORT must be used!
  # https://software.intel.com/en-us/node/535306
  # https://www.pgroup.com/resources/docs/19.4/x86/pgi-user-guide/index.htm#lib-dynlnk-bld-dll-fort
endif

# The GNU gfortran compiler flags "-fno-underscoring" (older f77:
# "-fno-underscore") and "-fno-second-underscore" will alter the default
# naming in the object code and thus affect linking. One may view the object
# file with the command nm (i.e.: nm file.o).
# http://www.yolinux.com/TUTORIALS/LinuxTutorialMixingFortranAndC.html
add_global_arguments(['-fno-underscoring'], language : 'fortran')

dynamic = shared_library('dynamic', 'dynamic.f')
exe = executable('test_exe', 'main.f', link_with : dynamic)
test('dynamic-fortran', exe)
