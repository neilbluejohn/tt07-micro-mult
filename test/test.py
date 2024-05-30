# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

# My imported code
import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import Timer
   
@cocotb.test()
async def micro_random_test(dut):

    # generate a clock
    
    cocotb.start_soon(Clock(dut.sys_clk, 10, units="ns").start())
   
    for i in range(1000):

        dut.nsys_rst.value = 0

        A = random.randint(0, 15)
        B = random.randint(0, 15)

        dut.ui[3:0].value = A
        dut.ui[7:4].value = B

        await Timer(200, units="ns")

        dut.nsys_rst.value = 1

        await Timer(1200, units="ns")

        assert dut.SMP_out.value == A * B, "Randomised test failed with: {A} * {B} = {X}".format(A=dut.inputA.value, B=dut.inputB.value, X=dut.SMP_out.value)




@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    assert dut.uo_out.value == 50

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
