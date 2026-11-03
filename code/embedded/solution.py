"""Synthetic plant-indicator logic. No physical actuator is controlled."""
import math


def relative_level(raw, dry, wet):
    if any(not math.isfinite(value) or not 0 <= value <= 1023 for value in (raw, dry, wet)):
        raise ValueError("readings must be finite ADC codes in 0..1023")
    if dry == wet:
        raise ValueError("dry and wet references must differ")
    if raw == dry:
        return 0.0
    return 100 * (raw - dry) / (wet - dry)


def warning_state(level, previous, enabled=True):
    if not math.isfinite(level):
        raise ValueError("level must be finite")
    if not enabled:
        return False
    if level < 30:
        return True
    if level > 40:
        return False
    return previous


def self_check():
    assert relative_level(800, 800, 300) == 0
    assert relative_level(300, 800, 300) == 100
    assert relative_level(550, 800, 300) == 50
    assert relative_level(550, 300, 800) == 50
    for previous in (False, True):
        for level in (30, 35, 40):
            assert warning_state(level, previous) == previous
        assert warning_state(29.9, previous)
        assert not warning_state(40.1, previous)
        assert not warning_state(0, previous, enabled=False)
    for raw, dry, wet in ((10, 20, 20), (-1, 800, 300), (float("nan"), 800, 300)):
        try:
            relative_level(raw, dry, wet)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid calibration/read accepted")
    state, outputs = False, []
    for level in (45, 29, 32, 39, 41):
        state = warning_state(level, state)
        outputs.append(state)
    assert outputs == [False, True, True, True, False]


if __name__ == "__main__":
    self_check()
    print("Checks passed.")
    state = False
    print("raw,relative_level,enabled,warning")
    for raw, enabled in [(575, True), (655, True), (640, True), (605, True), (595, True), (700, False)]:
        level = relative_level(raw, 800, 300)
        state = warning_state(level, state, enabled)
        print(f"{raw},{level:.1f},{enabled},{state}")
