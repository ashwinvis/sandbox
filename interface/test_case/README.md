# A simple test case for linking Fortran 77 -> C -> Python

The objective is to:

- [x] Build a shared library of a F77 source file: see `meow.f`
- [x] Clean up symbol names: no underscores (not portable?) / use
    `iso_c_binding`
- [ ] Call functions and subroutines from python: run `pytest -s` (WIP)


# Generating C headers

- https://gcc.gnu.org/onlinedocs/gfortran/Interoperability-Options.html

## Typing reference

- https://web.archive.org/web/20190720121337/http://northstar-www.dartmouth.edu/doc/solaris-forte/manuals/fortran/prog_guide/11_cfort.html
- https://cffi.readthedocs.io/en/latest/ref.html#conversions
