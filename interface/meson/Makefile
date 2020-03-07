lib := 9_cpp

all: clean
	@cd build/ && meson ../$(lib) && ninja

clean:
	@rm -rf build
	@mkdir -p build
