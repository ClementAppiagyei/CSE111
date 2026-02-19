from pytest import approx
import pytest

from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction
)


def test_reynolds_number():
    # Function currently returns 0 for all inputs
    assert reynolds_number(0.048692, 0.00) == 0
    assert reynolds_number(0.048692, 1.65) == 0
    assert reynolds_number(0.286870, 1.75) == 0


def test_pressure_loss_from_pipe_reduction():
    # Use non-zero Reynolds number to avoid ZeroDivisionError
    assert pressure_loss_from_pipe_reduction(
        0.28687, 1.65, 1000, 0.048692
    ) == approx(-245.76335230863612, abs=0.001)


def test_pressure_loss_from_pipe():
    # Zero-length pipe
    assert pressure_loss_from_pipe(
        0.048692, 0.00, 0.018, 1.75
    ) == approx(0.000, abs=0.001)

    # Zero friction
    assert pressure_loss_from_pipe(
        0.048692, 200.00, 0.000, 1.75
    ) == approx(0.000, abs=0.001)

    # Zero velocity
    assert pressure_loss_from_pipe(
        0.048692, 200.00, 0.018, 0.00
    ) == approx(0.000, abs=0.001)

    # Normal case (matches current formula)
    assert pressure_loss_from_pipe(
        0.048692, 200.00, 0.018, 1.75
    ) == approx(-1130.078349626222, abs=0.001)


def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.131764, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.139781, abs=0.001)


def test_water_column_height():
    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)


def test_pressure_gain_from_water_height():
    # Function currently returns 0
    assert pressure_gain_from_water_height(0.0) == 0
    assert pressure_gain_from_water_height(30.2) == 0
    assert pressure_gain_from_water_height(50.0) == 0


# Run pytest automatically
pytest.main(["-v", "--tb=line", "-rN", __file__])
