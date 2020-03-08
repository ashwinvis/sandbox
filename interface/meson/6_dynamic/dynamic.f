      subroutine hello
        implicit none
        integer n
        common /mycom/ n
        print *, "Hello from shared library."
        print *, "Fortran n =", n
      end subroutine
