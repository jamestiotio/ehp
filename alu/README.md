# 16-Bit Arithmetic Logic Unit (ALU) & ALU Tester

SUTD ISTD 2020 Computation Structures 1D ALU Project.

Team 03-2:

- James Raphael Tiovalen
- Ng Yu Yan
- Jodi Tan Kai Yu
- Cheow Wei Da Nicholas
- Sun Kairan



## Introduction

In this project, we implemented an Arithmetic Logic Unit (ALU) and its tester in the Alchitry Au FPGA.



## Features

This is the instruction set for the ALU.

> NOTE: X would indicate that that particular bit's value does not matter (whether it is a 0 or 1).

| ALUFN[5:0] | Operation              | Module       |
| ---------- | ---------------------- | ------------ |
| 00 00X0    | ADD                    | adder16      |
| 00 00X1    | SUBTRACT               | adder16      |
| 00 0100    | MULTIPLY               | multiplier16 |
| 00 0101    | FLOOR DIVISION         | multiplier16 |
| 00 0111    | MODULO                 | multiplier16 |
| 00 10X0    | INCREMENT X            | increment16  |
| 00 10X1    | INCREMENT Y            | increment16  |
| 00 11X0    | DECREMENT X            | decrement16  |
| 00 11X1    | DECREMENT Y            | decrement16  |
| 01 0000    | ZERO                   | boolean16    |
| 01 0001    | NOR                    | boolean16    |
| 01 0010    | NOT CONVERSE           | boolean16    |
| 01 0011    | NOT 'X'                | boolean16    |
| 01 0100    | NOT IMPLY              | boolean16    |
| 01 0101    | NOT 'Y'                | boolean16    |
| 01 0110    | XOR                    | boolean16    |
| 01 0111    | NAND                   | boolean16    |
| 01 1000    | AND                    | boolean16    |
| 01 1001    | XNOR                   | boolean16    |
| 01 1010    | 'X'                    | boolean16    |
| 01 1011    | IMPLY                  | boolean16    |
| 01 1100    | 'Y'                    | boolean16    |
| 01 1101    | CONVERSE               | boolean16    |
| 01 1110    | OR                     | boolean16    |
| 01 1111    | ONE                    | boolean16    |
| 10 XX00    | SHIFT LEFT             | shifter16    |
| 10 XX01    | SHIFT RIGHT            | shifter16    |
| 10 XX11    | SHIFT RIGHT ARITHMETIC | shifter16    |
| 11 X01X    | CMPEQ                  | comparator16 |
| 11 X10X    | CMPLT                  | comparator16 |
| 11 X11X    | CMPLE                  | comparator16 |



## Testing

For the ALU tester, we also have two modes: manual and automatic.

The main code in the `au_top.luc` file switches between the manual mode and the automatic mode when there is a button press detected from `io_button[2]`.