TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/four_bit_alu.v
TOPLEVEL = four_bit_alu
MODULE = four_bit_alu_tb
SIM = icarus
include $(shell cocotb-config --makefiles)/Makefile.sim