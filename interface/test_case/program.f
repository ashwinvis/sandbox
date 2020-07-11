c #define npow 1.2323
      program main

        include 'MEOW'
        ! real Cs

        ics = 1.5
        c = 123
        d = 123
        gamma = 1./3
        i = 1.1293812
        k = 1.2322
        onaksdnbakjsn = 1.1231
        zasdas = -1.23232
        print *, i, k, appa, u, x
        print *, ics
        print *, c
        print *, d
        print *, gamma

        print *, npow
        call set_meow(npow)
      end
