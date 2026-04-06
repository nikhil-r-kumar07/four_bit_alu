# 4-Bit ALU
A four-bit ALU that performs 8 different mathematical operations
## How it works
The ALU performs these mathematical operations:

- **ADD** - Adds two four-bit numbers and outputs a four bit number sum and a carry
- **SUBTRACT** - Subtracts two four-bit numbers and outputs a four bit number difference and a carry
- **AND** - Checks each corresponding bit of two four-bit numbers and outputs 1 for the bit if they are both one, otherwise 0
- **OR** - Checks each corresponding bit of two four-bit numbers and outputs 1 for the bit if at least one of them is one
- **XOR** - Checks each corresponding bit of two four-bit numbers and outputs 1 for the bit if only one is one
- **NOT** - Flips every bit of a four-bit number so that 1 becomes 0 and 0 becomes 1
- **SHIFT LEFT** - Shifts four-bit number left in the four-bit space
- **SHIFT RIGHT** - Shifts four-bit number right in the four-bit space
## Files
- `four_bit_alu.v` - RTL design
- `four_bit_alu_tb.py` - Python cocotb verification testbench
## How to Simulate
```bash
make
```
## Tools
Icarus Verilog, cocotb
## Status
Simulated and verified.