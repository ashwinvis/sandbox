F77:=gfortran
FFLAGS:= -std=legacy -fno-underscoring -fdefault-real-8 -fdefault-double-8 -O2
OBJS:=meow.o

program.out: program.f $(OBJS)
	$(F77) $^ $(FFLAGS) -o $@

libcat.so: meow.f MEOW
	$(F77) $< $(FFLAGS) -fPIC -shared -o $@

libcat.h: meow.f
	$(F77) $< $(FFLAGS) -fc-prototypes -fsyntax-only  > $@

%.o: %.f
	$(F77) -c $(FFLAGS) $<

clean:
	@rm -f *.o *.so *.out *.c

test:
	pytest -s
