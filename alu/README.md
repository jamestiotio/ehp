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

| ALUFN[5:0] | Operation              | Module       |
| ---------- | ---------------------- | ------------ |
| 00 0000    | ADD                    | adder16      |
| 00 X001    | SUBTRACT               | adder16      |
| 00 X010    | MULTIPLY               | multiplier16 |
| 00 X011    | DIVIDE                 | multiplier16 |
| 00 X100    | INCREMENTA             | increment16  |
| 00 X101    | INCREMENTB             | increment16  |
| 00 X110    | DECREMENTA             | decrement16  |
| 00 X111    | DECREMENTB             | decrement16  |
| 01 1000    | AND                    | boolean16    |
| 01 1110    | OR                     | boolean16    |
| 01 0110    | XOR                    | boolean16    |
| 01 1010    | 'A'                    | boolean16    |
| 01 1100    | 'B'                    | boolean16    |
| 01 0000    | ZERO                   | boolean16    |
| 01 1111    | ONE                    | boolean16    |
| 01 0111    | NAND                   | boolean16    |
| 01 1001    | XNOR                   | boolean16    |
| 01 0001    | NOR                    | boolean16    |
| 01 0101    | NOT 'A'                | boolean16    |
| 01 0011    | NOT 'B'                | boolean16    |
| 10 XX00    | SHIFT LEFT             | shifter16    |
| 10 XX01    | SHIFT RIGHT            | shifter16    |
| 10 XX11    | SHIFT RIGHT ARITHMETIC | shifter16    |
| 11 X00X    | ZERO                   | comparator16 |
| 11 X01X    | CMPEQ                  | comparator16 |
| 11 X10X    | CMPLT                  | comparator16 |
| 11 X11X    | CMPLE                  | comparator16 |




## Testing

For the ALU tester, we also have two modes: manual and automatic.
