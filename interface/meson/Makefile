lib := 6_dynamic
build := build

all:
	@printf '\n============================ Step 1: Meson ==================================\n'
	@meson setup $(build) $(lib)
	@printf '\n============================ Step 2: Ninja ==================================\n'
	@ninja -C $(build) -v
	@printf '\n========================= Step 3: Python CFFI ===============================\n'
	@python $(lib).py

clean:
	@rm -rf $(build)
