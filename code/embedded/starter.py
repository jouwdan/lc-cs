"""Synthetic calibration: change the readings before changing the formula."""
import math

def relative_level(raw, dry, wet):
    if any(not math.isfinite(value) or not 0 <= value <= 1023 for value in (raw, dry, wet)):
        raise ValueError("readings must be finite ADC codes in 0..1023")
    if dry == wet:
        raise ValueError("dry and wet references must differ")
    if raw == dry:
        return 0.0
    return 100 * (raw - dry) / (wet - dry)



dry = 800
wet = 300
raw_readings = [800, 550, 300]
for raw in raw_readings:
    level = relative_level(raw, dry, wet)
    print(f"Raw {raw} -> relative level {level:.1f}")
