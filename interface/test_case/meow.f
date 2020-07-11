
      subroutine init_cat(purr)
        include 'MEOW'

        cat = 42.0
      end subroutine

      function get_cat() result(cat_for_export)
        include 'MEOW'
        real cat_for_export

        cat_for_export = cat
      end function

      subroutine set_meow(purr)
        include 'MEOW'
        real purr
c
        cat = cat + purr
        print *, "Fortran says cat =", cat, "purr = ", purr

      end subroutine

      subroutine cset_meow(purr) bind(C)
        use iso_c_binding
        include 'MEOW'

        real(c_double) purr

c
        cat = cat + purr
        print *, "Fortran says cat =", cat, "purr = ", purr

      end subroutine
