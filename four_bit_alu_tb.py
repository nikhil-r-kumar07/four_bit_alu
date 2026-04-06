import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_add(dut):
    dut.opcode.value = 0
    dut.A.value = 15
    dut.B.value = 1
    await Timer(1, units = "ns")
    assert dut.result.value == 0, "ADD operation takes the last four digits correctly"
    assert dut.carry.value == 1, "Carry operation works perfectly"

@cocotb.test()
async def test_subtract(dut):
    dut.opcode.value = 1
    dut.A.value = 2
    dut.B.value = 3
    await Timer(1, units = "ns")
    assert dut.result.value == 15, "SUBTRACT operation works perfectly"
    assert dut.carry.value == 1, "Carry operation works perfectly"

@cocotb.test()
async def test_and(dut):
    dut.opcode.value = 2
    dut.A.value = 9
    dut.B.value = 12
    await Timer(1, units = "ns")
    assert dut.result.value == 8, "AND operation works perfectly"

@cocotb.test()
async def test_or(dut):
    dut.opcode.value = 3
    dut.A.value = 9
    dut.B.value = 12
    await Timer(1, units = "ns")
    assert dut.result.value == 13, "OR operation works perfectly"

@cocotb.test()
async def test_xor(dut):
    dut.opcode.value = 4
    dut.A.value = 9
    dut.B.value = 12
    await Timer(1, units = "ns")
    assert dut.result.value == 5, "XOR operation works perfectly"

@cocotb.test()
async def test_not(dut):
    dut.opcode.value = 5
    dut.A.value = 9
    await Timer(1, units = "ns")
    assert dut.result.value == 6, "Not operation works perfectly"

@cocotb.test()
async def test_shift_left(dut):
    dut.opcode.value = 6
    dut.A.value = 9
    await Timer(1, units = "ns")
    assert dut.result.value == 2, "Shift left operation works perfectly"

@cocotb.test()
async def test_shift_right(dut):
    dut.opcode.value = 7
    dut.A.value = 9
    await Timer(1, units = "ns")
    assert dut.result.value == 4, "Shift right operation works perfectly"