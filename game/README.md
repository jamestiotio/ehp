# Chopsticks

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

## Tests

These tests are available inside/within the `tests` folder:

- `BrPinTest`: Test the operability of each SingleEndedIO pin of the custom Alchitry Br board.
- `ButtonTest`: Test the functionality of a set of button and an LED (button is connected to VDD and `B30`, while LED is connected to `B21`, resistor and GND).
- `ButtonPressTest`: Test the functionality of the complete circuitry to debug any potential/possible connection problems due to poor soldering/wiring.

## Known Current Issues

1. For normal attacks and results of splitting, current `ADD` of 1 is stuck at a constant value of 6 (register number of `from`) and current `MOD` is stuck at a constant value of 16 (only lowest 4 bits stored in REGFILE for each hand).

2. Off-by-one error for SPLIT and POWERUP cycles.

3. POWERUP cycle is `MOD` by a constant value of 7 instead of 9.

4. Implement check to not allow splitting/transferring to the same hand (this will also address the issue of accidental multiple-clicking button signal detection due to unstable/unreliable wiring/soldering connections).

5. Manual reset button needs to also reset all of the REGFILE's DFFs to their original initial values.

## Future Work

- Scoring system using persistent data
- Audio/sound/music player using a speaker/buzzer
- Add more proper game logic testers