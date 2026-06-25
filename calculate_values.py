# ============================================
# Touch Sensor Circuit — Component Value Calculator
# ============================================

# Power Supply
Vcc = 9.0        # Battery voltage (V) — AA battery

# LED Parameters (D1)
Vf  = 2.0        # LED forward voltage (V)
If  = 0.020      # LED desired current — 20mA

# BC547 Transistor Parameters (Q1, Q3)
hFE_Q1 = 100     # Current gain of Q1
hFE_Q3 = 100     # Current gain of Q3
hFE_darlington = hFE_Q1 * hFE_Q3  # Darlington pair total gain

# ============================================
# R2 — Current Limiting Resistor (protects LED)
# Formula: R2 = (Vcc - Vf) / If
# ============================================

R2 = (Vcc - Vf) / If

print("=" * 45)
print("  Touch Sensor Circuit — Value Calculator")
print("=" * 45)

print("\n--- Power Supply ---")
print(f"  Vcc (battery voltage) : {Vcc} V")

print("\n--- LED (D1) ---")
print(f"  Forward voltage (Vf)  : {Vf} V")
print(f"  Desired current (If)  : {If * 1000:.0f} mA")
print(f"  R2 calculated value   : {R2:.1f} ohms")
print(f"  R2 standard value     : 390 ohms (closest standard)")

# ============================================
# R1 — Base Resistor (controls Q3 base current)
# Formula: Ib = Ic / hFE, R1 = Vcc / Ib
# ============================================

Ic     = If                        # Collector current ≈ LED current
Ib_Q1  = Ic / hFE_Q1              # Base current needed for Q1
Ib_Q3  = Ib_Q1 / hFE_Q3          # Base current needed for Q3 (Darlington)
R1     = Vcc / Ib_Q3              # Max R1 value

print("\n--- Darlington Pair (Q3 + Q1 BC547) ---")
print(f"  hFE Q3                : {hFE_Q3}")
print(f"  hFE Q1                : {hFE_Q1}")
print(f"  Total Darlington gain : {hFE_darlington}")
print(f"  Collector current     : {Ic * 1000:.0f} mA")
print(f"  Base current (Q3)     : {Ib_Q3 * 1_000_000:.2f} uA")
print(f"  R1 calculated value   : {R1:.1f} ohms")
print(f"  R1 standard value     : 1M ohm (allows finger resistance to trigger)")

print("\n--- Touch Plate (TP1) ---")
print("  Human skin resistance : ~1k - 100k ohms")
print("  Acts as variable resistor between Vcc and Q3 base")
print("  Darlington pair amplifies tiny touch current to drive LED")

print("\n--- Summary ---")
print(f"  R1 : 1M ohm   — base resistor")
print(f"  R2 : 390 ohm  — LED current limiter")
print(f"  Q1 : BC547 NPN transistor")
print(f"  Q3 : BC547 NPN transistor")
print(f"  D1 : Standard 5mm LED")
print(f"  BT1: AA Battery (9V or 1.5V x6)")
print("=" * 45)