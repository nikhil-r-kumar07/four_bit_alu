module fourbitalu (
    input [3:0] A, B,
    input [2:0] opcode,
    output [3:0] result,
    output carry,
    output zero
);

reg [3:0] result;
reg carry;
always @(*) begin
    case (opcode) begin
        3'b000 : A + B;
        3'b001 : A - B;
        3'b010 : A & B;
        3'b011 : A | B;
        3'b100 : A ^ B;
        3'b101 : ~A;
        3'b110 : A - 1;
        3'b111 : A + 1;
    end
end
endmodule