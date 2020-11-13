# Digisticks Game Documentation

## Table 1: REGFILE

+ 16 16-bit Registers (@ 4-bit addressable)
+ 2 addressable combinational READ ports
+ 7 fixed combinational READ ports
+ 1 sequential WRITE port

| Register | Usage                 | Register | Usage   |
| -------- | --------------------- | -------- | ------- |
| R0       | P1 Right Hand         | R8       | LITERAL |
| R1       | P1 Left Hand          | R9       | POWERUP |
| R2       | P2 Right Hand         | R10      | WINNER  |
| R3       | P2 Left Hand          | R11      | TURN    |
| R4       | P1 Remaining Powerups | R12      | TEMP    |
| R5       | P2 Remaining Powerups | R13      | TEMP    |
| R6       | FROM                  | R14      | TEMP    |
| R7       | TO                    | R15      | 0       |

 #### Remarks:
   + P1: Player 1
   + P2: Player 2
   + LITERAL: number for splitting
   + FROM and TO: stores the addresses of the two registers (hands) to do operations on
   + WINNER: 0 (NONE), 1 (P1 WIN), 2 (P2 WIN)
   + TURN: 0 (P1), 1 (P2)
   + R15: Always ZERO



## Table 2: Overview of States & Transitions
|       | START | Powerups               | Attack  | Split       | Choose Split | Choose Powerup | Reset                     | Check P1/P2 | Update Turn | Win  | Waiting for FROM | Store FROM  | Store TO    | GAME OVER |
| ----- | ----- | ---------------------- | ------- | ----------- | ------------ | -------------- | ------------------------- | ----------- | ----------- | ---- | ---------------- | ----------- | ----------- | --------- |
| ALUFN | -     | ADD/BOOLEAN CHOICE/MOD | ADD/MOD | ADD/MOD/SUB | -/ADD/CMPLE  | ADD/MOD        | ADD/-/-/-                 | CMPEQ       | XOR         | ADD  | -                | 'X'/-/'X'/- | 'X'/-/'X'/- | -         |
| ASEL  | -     | 0                      | 0       | 0           | -/0/0        | 0              | 0/-/-/-                   | 0           | 0           | 0    | -                | 0/-/1/-     | 0/-/1/-     | -         |
| BSEL  | -     | 00/00/10               | 00/10   | 00/10/00    | -/01/00      | 01/11          | 00/-/-/-                  | 00          | 01          | 01   | -                | -           | -           | -         |
| WDSEL | -     | 00/00/00               | 00      | 00          | 01/01/00     | 00             | 00/01/10/01               | 00          | 00          | 00   | -                | 00/01/00/10 | 00/01/00/10 | -         |
| Ra    | -     | R15/TO/TO              | TO/TO   | R8/TO/R8    | R8           | R9             | R15/-/-/-                 | R0&R1/R2&R3 | R11         | R11  | -                | R15/-/-/-   | R15/-/-/-   | -         |
| Rb    | -     | R9/FROM/-              | FROM/-  | TO/-/FROM   | -/-/FROM     | -              | R15/-/-/-                 | R15         | -           | -    | -                | -           | -           | -         |
| Rc    | -     | R15/TO/TO              | TO/TO   | TO/TO/FROM  | R8/R8/R15    | R9             | R[6:10]/R[0:3]/R[4:5]/R11 | R15         | R11         | R10  | -                | R6          | R7          | -         |

+ REMARK: FROM and TO here and below refer to inputs to Control Unit, which are the values stored in R6 and R7 respectively.

### Table 2.1: RESET 

Green in diagram

|       | RESET HANDS | RESET TO ZERO | RESET POWERUP | RESET TURN |
| ----- | ----------- | ------------- | ------------- | ---------- |
| ALUFN | -           | ADD           | -             | -          |
| ASEL  | -           | 0             | -             | -          |
| BSEL  | -           | 00            | -             | -          |
| WDSEL | 01          | 00            | 10            | 01         |
| Ra    | -           | R15           | -             | -          |
| Rb    | -           | R15           | -             | -          |
| Rc    | R[0:3]      | R[6:10]       | R[4:5]        | R11        |

### Table 2.2: POWERUP MODE

Red in diagram.

+ STEP 1: CHOOSE POWERUP 

    |       | AND  | OTHER BOOLEAN CHOICES |
    | ----- | ---- | --------------------- |
    | ALUFN | -    | ADD/MOD               |
    | ASEL  | -    | 0                     |
    | BSEL  | -    | 01/11                 |
    | WDSEL | 01   | 00                    |
    | Ra    | -    | R9                    |
    | Rb    | -    | -                     |
    | Rc    | R9   | R9                    |

+ STEP 2: DO OPERATION AFTER CONFIRM

    |       | STORE FROM  | STORE TO    | READ R9 | DO             | MOD  |
    | ----- | ----------- | ----------- | ------- | -------------- | ---- |
    | ALUFN | 'X'/-/'X'/- | 'X'/-/'X'/- | ADD     | BOOLEAN CHOICE | MOD  |
    | ASEL  | 0/-/1/-     | 0/-/1/-     | 0       | 0              | 0    |
    | BSEL  | -           | -           | 00      | 00             | 10   |
    | WDSEL | 00/01/00/10 | 00/01/00/10 | 00      | 00             | 00   |
    | Ra    | R15/-/-/-   | R15/-/-/-   | R15     | TO             | TO   |
    | Rb    | -           | -           | R9      | FROM           | -    |
    | Rc    | R6          | R7          | R15     | TO             | TO   |
    
    + READ R9, DO and MOD are in state DO OP MOD.
    
    + The contents of R9 (contains powerup chosen) will be routed through the ALU output to the Control Unit, which will be used to determine the ALUFN at DO.
    
    + STORE FROM and STORE TO store the addresses of the registers that we are transferring from and to.
    
    + Refer to remarks for further explanation of STORE FROM and STORE TO.
    
    + We define the correspondence of values in R9 to BOOLEAN CHOICES below:
    
      | VALUE IN R9 | BOOLEAN CHOICES |
      | ----------- | --------------- |
      | 0000        | NOT'Y'          |
      | 0001        | AND             |
      | 0010        | NAND            |
      | 0011        | OR              |
      | 0100        | NOR             |
      | 0101        | XOR             |
      | 0110        | XNOR            |
      | 0111        | 'X'             |
      | 1000        | NOT'X'          |
    

### Table 2.3: NORMAL MODE

Black in diagram for step 1 and 2.. Light Blue for step 2.2.

+ STEP 1: STORE IN FROM IF CHOSEN Reg[FROM] != 0

    |       | CHECK HAND  | STORE IN FROM |
    | ----- | ----------- | ------------- |
    | ALUFN | CMPEQ       | 'X'/-/'X'/-   |
    | ASEL  | 0           | 0/-/1/-       |
    | BSEL  | 00          | -             |
    | WDSEL | 00          | 00/01/00/10   |
    | Ra    | R0/R1/R2/R3 | R15/-/-/-     |
    | Rb    | R15         | -             |
    | Rc    | R15         | R6            |

    + Ra being R0/R1/R2/R3 depends on which button has been pressed
    + The ALU output is connected to the Control Unit, such that if the output is 1 (true that R0/R1/R2/R3 is 0), we go to back to P1. If the output is 0, we go to STORE IN FROM.

+ STEP 2.1: GO TO ATTACK

    |       | STORE IN TO | ADD  | MOD  |
    | ----- | ----------- | ---- | ---- |
    | ALUFN | X/-/X/-     | ADD  | MOD  |
    | ASEL  | 0/-/1/-     | 0    | 0    |
    | BSEL  | -           | 00   | 10   |
    | WDSEL | 00/01/00/10 | 00   | 00   |
    | Ra    | R15/-/-/-   | TO   | TO   |
    | Rb    | -           | FROM | -    |
    | Rc    | R7          | TO   | TO   |

+ STEP 2.2: GO TO SPLIT

    |       | STORE IN TO | 2? 3? 4? | 1?   | CHECK FROM>X | ADD  | MOD  | SUB  |
    | ----- | ----------- | -------- | ---- | ------------ | ---- | ---- | ---- |
    | ALUFN | 'X'/-/'X'/- | ADD      | -    | CMPLE        | ADD  | MOD  | SUB  |
    | ASEL  | 0/-/1/-     | 0        | -    | 0            | 0    | 0    | 0    |
    | BSEL  | -           | 01       | -    | 00           | 00   | 10   | 00   |
    | WDSEL | 00/01/00/10 | 00       | 01   | 00           | 00   | 00   | 00   |
    | Ra    | R15/-/-/-   | R8       | -    | R8           | R8   | TO   | R8   |
    | Rb    | -           | -        | -    | FROM         | TO   | -    | FROM |
    | Rc    | R7          | R8       | R8   | R15          | TO   | TO   | FROM |

    + NOTE: CHOOSING and CHECK form a loop to choose how much to split. Only when POWERUP button is pressed to confirm the choice, it will move on to do SUB, ADD and MOD.
    + The ALU output from CHECK FROM>X will determine the next state. 1 - moves on to 2?/3?/4?. 0 - goes back to 1?

### Table 2.4: CHECK P1/P2

Orange in diagram.

|       | CHECK RIGHT HAND | CHECK LEFT HAND | P1/P2 WINS |
| ----- | ---------------- | --------------- | ---------- |
| ALUFN | CMPEQ            | CMPEQ           | ADD        |
| ASEL  | 0                | 0               | 0          |
| BSEL  | 00               | 00              | 01         |
| WDSEL | 00               | 00              | 00         |
| Ra    | R0/R2            | R1/R3           | R11        |
| Rb    | R15              | R15             | -          |
| Rc    | R15              | R15             | R10        |

+ Ra:
  + R0 and R1 when CHECK P1.
  + R2 and R3 when CHECK P2.
+ P1/P2 WINS updates R10 with the winner.

### Table 2.5: UPDATE TURN

Purple in diagram.

|       | P1 and P2 |
| ----- | --------- |
| ALUFN | XOR       |
| ASEL  | 0         |
| BSEL  | 01        |
| WDSEL | 00        |
| Ra    | R11       |
| Rb    | -         |
| Rc    | R11       |

### Table 2.6: WAITING STATES

Dark Blue in diagram.

|       | START | GAME OVER | WAIT FOR FROM |
| ----- | ----- | --------- | ------------- |
| ALUFN | -     | -         | -             |
| ASEL  | -     | -         | -             |
| BSEL  | -     | -         | -             |
| WDSEL | -     | -         | -             |
| Ra    | -     | -         | -             |
| Rb    | -     | -         | -             |
| Rc    | -     | -         | -             |



### Table 2.7: STORE IN FROM/TO IN DETAILS

+ In order to minimize the the output of CU, we will use different ways to get the address which we want to store in FROM and AND.
+ Details are shown in the table below. If STORE IN FROM, Rc will be R6. If STORE IN TO, Rc will be R7.

|       | IF P1R | IF P1L | IF P2R | IF P2L |
| ----- | ------ | ------ | ------ | ------ |
| ALUFN | X      | -      | X      | -      |
| ASEL  | 0      | -      | 1      | -      |
| BSEL  | -      | -      | -      | -      |
| WDSEL | 00     | 01     | 00     | 10     |
| Ra    | R15    | -      | -      | -      |
| Rb    | -      | -      | -      | -      |
| Rc    | R6/R7  | R6/R7  | R6/R7  | R6/R7  |

 