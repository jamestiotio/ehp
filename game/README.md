# DigiSticks

SUTD ISTD 2020 Computation Structures 1D Electronic Game Project.

Team 03-2:

- James Raphael Tiovalen
- Ng Yu Yan
- Jodi Tan Kai Yu
- Cheow Wei Da Nicholas
- Sun Kairan

## Introduction

> Chopsticks is a hand game for two or more players, in which players extend a number of fingers from each hand and transfer those scores by taking turns to tap one hand against another. Chopsticks is an example of a combinatorial game, and is solved in the sense that with perfect play, an optimal strategy from any point is known.

For our project, we digitalize this hand game and initiated some reworking and remodeling of the whole design process. We utilize the variant with remainders and transfers, with an additional extension of including boolean operations into the game (instead of just additions and modulos).

For circuitry wiring, connect as such:

- Buttons to VDD and IO pins
- LEDs to appropriate resistors, IO pins and GND
- 7-segments' pins to appropriate resistors (except for the 4 digit selectors) and IO pins

Follow the correspondingly attached circuit wiring schematics diagram.

> NOTES:
>
> We attempted to build our own custom hardware & circuitry datapath and FSM specific to this game instead of just emulating the unpipelined 32-bit general-purpose Beta ISA. This is so that we could gain some experience on building our own electrical circuitry.
>
> Most electronics components were obtained from Sim Lim Tower located in Singapore.
>
> A minor note on choice of button placements: to each player, we allocated 2 buttons which refer to their respective opponent's hand instead of just allocating their own hands' buttons (where they could actually reach out to the other player's side and press the opponent's buttons to indicate their selected target hand). The reason for this is due to `sOcIaL dIsTaNcInG`.

## Tests

These tests are available inside/within the `tests` folder:

- `BrPinTest`: Test the operability of each SingleEndedIO pin of the custom Alchitry Br board.
- `ButtonTest`: Test the functionality of a set of button and an LED (button is connected to VDD and `B30`, while LED is connected to `B21`, resistor and GND).
- `ButtonPressTest`: Test the functionality of the complete circuitry to debug any potential/possible connection problems due to poor soldering/wiring.

## Known Current Issues

1. For normal attacks (and potentially results of powerup and splitting), current `ADD` of 1 is stuck at a constant value of 6 (register number of `from`) and current `MOD` is stuck at a constant value of 16 (only lowest 4 bits stored in REGFILE for each hand; I suspect the MODULO function is not even running).

2. Off-by-one error for SPLIT and POWERUP cycles.

3. POWERUP cycle is `MOD` by a constant value of 6 instead of 9.

4. Implement check to not allow splitting/transferring to the same hand (this will also address the issue of accidental multiple-clicking button signal detection due to unstable/unreliable wiring/soldering connections).

5. Manual reset button needs to also reset all of the REGFILE's DFFs to their original initial values.

## Future Work

- Scoring system using persistent data
- Audio/sound/music player using a speaker/buzzer
- Add more proper game logic testers
- Add current player indicator
- Add game over WIN/LOSE message indicator
- Somehow rebalance the POWERUP abilities (since for now, they are so powerful that an opponent can be defeated in 2-4 moves if the first player is playing optimally)
- More players?
- More creative and innovative elements?
