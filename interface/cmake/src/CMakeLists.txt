cmake_minimum_required(VERSION 3.16)

project(foobar VERSION 0.1.0 LANGUAGES Fortran C)
set(DEFAULT_BUILD_TYPE "Release")

add_library(foo SHARED foo.f)
# add_executable(bar bar.c)
# target_link_libraries(bar foo)
target_link_libraries(foo)
set_target_properties(foo PROPERTIES VERSION ${PROJECT_VERSION})


include(FortranCInterface)
FortranCInterface_HEADER(
    cfoo.h
    MACRO_NAMESPACE "foo_"
    # SYMBOL_NAMESPACE ""
    SYMBOLS add
    # mymod:my_sub
)
