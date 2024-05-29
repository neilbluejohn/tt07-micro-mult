module tt_um_njp_micro(input sys_clk, nsys_rst, input [3:0] inputA, inputB, output [7:0] SMP_out);
  
  wire sys_rst, flag, C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12;
  
  assign sys_rst = !nsys_rst;
  
  ControlUnit P1(.sys_clk(sys_clk), .sys_rst(sys_rst), .flag(flag), .C0(C0), .C1(C1), .C2(C2), .C3(C3), .C4(C4), .C5(C5), .C6(C6), .C7(C7), .C8(C8), .C9(C9), .C10(C10), .C11(C11), .C12(C12));

  DataPath P2(.sys_clk(sys_clk), .sys_rst(sys_rst), .flag(flag), .inputA(inputA), .inputB(inputB), .SMP_out(SMP_out), .enA(C0), .enB(C1), .enDPO(C2), .ABsel(C3), .sr_c1(C4), .sr_c0(C5), .enSR(C6), .SRsel(C7), .alu_c0(C8), .alu_c1(C9), .alu_c2(C10), .enACC(C11), .clrACC(C12));

initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1, SMP_out, sys_clk, nsys_rst, inputA, inputB);
end
  
endmodule