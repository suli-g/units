"""
Implements the Unit model for this application.

Models:
- Unit: Represents a unit of measurement.
"""

from typing import Iterable, Optional
from django.db import models


class Unit(models.Model):
    """
    Represents a unit of measurement.

    Properties:
        name: The name of the unit.
        symbol: The symbol of the unit.
        scale: The scale of the unit, defaults to 1.0.
        base: The base unit, if any.
    """

    name: models.CharField = models.CharField( # type: ignore
        verbose_name="Unit Name", unique=True, max_length=32
    )
    """ The name of the unit. """
    base: models.ForeignKey = models.ForeignKey(
        "Unit", on_delete=models.CASCADE, null=True, blank=True
    )
    """ The base unit, if any. """
    symbol: models.CharField = models.CharField(
        verbose_name="Unit Symbol", max_length=20
    )
    """ The symbol of the unit. """
    scale: models.FloatField = models.FloatField(
        verbose_name="Unit Scale", default=1.0
    )
    """ The scale of the unit, defaults to 1.0. """

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: Optional[str] = None,
        update_fields: Optional[Iterable[str]] = None,
    ) -> None:
        """
        Overrides the default save method for this model, ensuring that only
        base units may have a scale of 1.0.

        Parameters:
            force_insert:
                Forces the SQL statement used for saving to be an INSERT,
                defaults to False.
            force_update:
                Forces the SQL statement used for saving to be an UPDATE,
                defaults to False.
            using: The database alias to use for the query.
            update_fields: The fields to update, if any.
        Raises:
            AttributeError: If this unit has both a base and a scale of 1.0.
        """
        if self.base is not None and self.scale == 1.0:
            raise AttributeError("Sub units may not have a scale of 1.0.")
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self) -> str:
        """
        Returns a string representation of this unit, including a comparison
        to the base unit if this is a subunit, otherwise just the symbol.
        """
        if self.base is None:
            return self.symbol
        return f"{self.symbol} ({self.scale} x {self.base.symbol})"
