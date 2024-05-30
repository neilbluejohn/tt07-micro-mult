# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

# My imported code
import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import Timer
   
@cocotb.test()
async def micro_random_test(dut):
    #dut._log.info("Start")
    # generate a clock
    
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
   
    for i in range(1000):

        dut.rst_n.value = 0

        A = random.randint(0, 255)
   

        dut.ui_in[7:0].value = A
        #dut.ui_in[7:4].value = B

        await Timer(200, units="ns")

        dut.rst_n.value = 1

        await Timer(1200, units="ns")

        assert dut.SMP_out.value == A[7:4] * B[7:4], "Randomised test failed with: {A} * {B} = {X}".format(A=dut.inputA.value, B=dut.inputB.value, X=dut.SMP_out.value)



    

    # Set the clock period to 10 us (100 KHz)

    # Reset
    #dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    
    dut._log.info("Test project behavior")

    
    
    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
