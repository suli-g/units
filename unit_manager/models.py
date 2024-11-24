"""
Implements the Unit model for this application.

Models:
- Unit: Represents a unit of measurement.
"""

from typing import Optional
from django.db import models


class Unit(models.Model):
    """
    Represents a unit of measurement.

    Properties:
    - name: The name of the unit.
    - symbol: The symbol of the unit.
    - scale: The scale of the unit, defaults to 1.0.
    - base: The base unit, if any.
    """

    name: str = models.CharField(verbose_name="Unit Name", unique=True, max_length=32)
    """ The name of the unit. """
    base: Optional["Unit"] = models.ForeignKey(
        "Unit", on_delete=models.CASCADE, null=True, blank=True
    )
    """ The base unit, if any. """
    symbol: str = models.CharField(verbose_name="Unit Symbol", max_length=20)
    """ The symbol of the unit. """
    scale: float = models.FloatField(verbose_name="Unit Scale", default=1.0)
    """ The scale of the unit, defaults to 1.0. """

    def save(self, *args, **kwargs) -> None:
        """
        Overrides the default save method for this model, ensuring that only
        base units may have a scale of 1.0.


        Raises:
            ValidationError: If this unit has both a base and a scale of 1.0.
        """
        if self.base is not None and self.scale == 1.0:
            raise AttributeError("Sub units may not have a scale of 1.0.")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """Returns a string representation of this unit, including a comparison
        to the base unit if this is a subunit, otherwise just the symbol."""
        if self.base is None:
            return self.symbol
        return f"{self.symbol} ({self.scale} x {self.base.symbol})"
