c #define npow 1.2323
      program main

        include 'MEOW'

        call init_cat()
        print *, "After init:", cat
        call set_meow(cat)
        print *, "After set:", cat
        print *, cat, "\n"
      end
