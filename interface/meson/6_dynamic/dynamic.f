      subroutine hello()  bind(C)
        use iso_c_binding
        implicit none
        print *, "Hello from shared library."
      end subroutine
