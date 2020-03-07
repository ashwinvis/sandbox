all: clean
	@cd build/ && cmake ../src
	@bat build/cfoo.h
	@cd build/ && make

clean:
	@rm -rf build
	@mkdir -p build
