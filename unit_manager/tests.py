import pytest
from django.db.utils import IntegrityError
from .models import Unit


@pytest.fixture
def base_unit(db):
    """Fixture to create a base unit."""
    return Unit.objects.create(name="Meter", symbol="m", scale=1.0)


@pytest.mark.django_db
def test_create_base_unit(base_unit):
    """Test creating a base unit with no parent and scale of 1.0."""
    assert base_unit.name == "Meter"
    assert base_unit.symbol == "m"
    assert base_unit.base is None
    assert base_unit.scale == 1.0


@pytest.mark.django_db
def test_create_subunit_with_valid_scale(base_unit):
    """Test creating a subunit with a valid scale."""
    subunit = Unit.objects.create(
        name="Centimeter", symbol="cm", base=base_unit, scale=0.01
    )
    assert subunit.name == "Centimeter"
    assert subunit.symbol == "cm"
    assert subunit.base == base_unit
    assert subunit.scale == 0.01


@pytest.mark.django_db
def test_subunit_with_invalid_scale_raises_error(base_unit):
    """Test creating a subunit with a scale of 1.0 raises an error."""
    with pytest.raises(
        AttributeError, match="Sub units may not have a scale of 1.0."
    ):
        Unit.objects.create(
            name="InvalidSubunit", symbol="is", base=base_unit, scale=1.0
        )


@pytest.mark.django_db
def test_unit_symbol_str(base_unit):
    """Test the string representation of a base unit."""
    assert str(base_unit) == "m"


@pytest.mark.django_db
def test_subunit_symbol_str(base_unit):
    """Test the string representation of a subunit."""
    subunit = Unit.objects.create(
        name="Centimeter", symbol="cm", base=base_unit, scale=0.01
    )
    assert str(subunit) == "cm (0.01 x m)"


@pytest.mark.django_db
def test_unit_name_uniqueness_constraint(db):
    """Test that the `name` field enforces uniqueness."""
    Unit.objects.create(name="Meter", symbol="m", scale=1.0)
    with pytest.raises(IntegrityError):
        Unit.objects.create(name="Meter", symbol="m2", scale=2.0)
