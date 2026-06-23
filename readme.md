# Touch Sensor Circuit — KiCad Project

A capacitive touch sensor circuit designed in KiCad that lights up an LED when the touch plate is activated. Built using a Darlington pair transistor configuration for high current gain amplification.

---

## How the Circuit Works

When the touch plate (TP1) is activated by a finger, the human body acts as a resistor and allows a small current to flow into the base of the first transistor (Q3) through the base resistor (R1). This small current is amplified by Q3 and fed directly into the base of the second transistor (Q1), forming a Darlington pair configuration.

The Darlington pair provides very high current gain (hFE × hFE), meaning even the tiny current from a finger touch is enough to fully switch on both transistors. Once Q1 is switched on, current flows through the collector-emitter path, through the current limiting resistor (R2) and the LED (D1), causing the LED to light up.

When the finger is removed from the touch plate, the base current drops to zero, both transistors switch off, and the LED turns off.

---

## Components

| Reference | Component | Description |
|-----------|-----------|-------------|
| TP1 | Touch Plate | Input — finger touch activates the circuit |
| R1 | Resistor | Base resistor, limits current into Q3 base |
| Q3 | BC547 NPN | First transistor in Darlington pair |
| Q1 | BC547 NPN | Second transistor in Darlington pair |
| R2 | Resistor | Current limiting resistor, protects the LED |
| D1 | LED | Output indicator, lights up on touch |
| BT1 | AA Battery | Power supply (Vcc) |

---

## Project Files

| File | Description |
|------|-------------|
| `touchSensor.kicad_sch` | Schematic diagram |
| `touchSensor.kicad_pcb` | PCB layout |
| `touchSensor.kicad_pro` | KiCad project file |
| `touchSensor.kicad_prl` | Project local settings |
| `gerbers/` | Gerber manufacturing files |
| `readme.pdf` | Project documentation |

---

## Gerber Files

| File | Layer |
|------|-------|
| `touchSensor-F_Cu.gbr` | Front copper layer |
| `touchSensor-B_Cu.gbr` | Back copper layer |
| `touchSensor-F_Mask.gbr` | Front solder mask |
| `touchSensor-B_Mask.gbr` | Back solder mask |
| `touchSensor-F_Silkscreen.gbr` | Front silkscreen |
| `touchSensor-B_Silkscreen.gbr` | Back silkscreen |
| `touchSensor-Edge_Cuts.gbr` | Board outline |
| `touchSensor-PTH.drl` | Plated drill holes |
| `touchSensor-NPTH.drl` | Non-plated drill holes |

---

## Tools Used

- KiCad 10.0
