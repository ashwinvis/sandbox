lib := 6_dynamic

all: clean
	@cd build/ && meson ../$(lib) && ninja
	@echo "-------------------------------"
	@python $(lib).py

clean:
	@rm -rf build
	@mkdir -p build
