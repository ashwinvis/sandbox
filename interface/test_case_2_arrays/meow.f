      subroutine init_cat()
        include 'MEOW'

        cat = reshape((/ 1, 2, 3, 4, 5, 6, 7, 8, 9 /), shape(cat))
      end subroutine

      subroutine get_cat(cat_for_export_ptr) bind(C)
        use iso_c_binding
        include 'MEOW'

        ! https://stackoverflow.com/q/28351919
        real(c_double) cat_for_export(3, 3)
        target cat_for_export

        type(c_ptr) cat_for_export_ptr

        ! cat_for_export(:, :) = cat(:, :)
        cat_for_export = cat
        cat_for_export_ptr = c_loc(cat_for_export)
      end subroutine

      subroutine set_meow(purr)
        include 'MEOW'
        real purr(3, 3)
c
        cat = cat + purr
        print *, "Fortran says cat =", cat
        print *, "purr = ", purr

      end subroutine

      subroutine cset_meow(purr) bind(C)
        use iso_c_binding
        include 'MEOW'

        real(c_double) purr(3, 3)

c
        cat = cat + purr
        print *, "Fortran says cat =", cat
        print *, "purr = ", purr

      end subroutine
