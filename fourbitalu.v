module 4bitalu (
    input [3:0] A, B,
    input [2:0] opcode,
    output [3:0] result,
    output carry,
    output zero
);

reg [3:0] result;
