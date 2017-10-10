#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6. Conversions"""

import decimal


def convertCelsiusToKelvin(degrees):
    """Converting Celsium measurment to Kevins
    Args:
        degrees(int, float): number of degrees to convert
    Returns:
        conversion
    Example:
        >>> convertCelsiusToKelvin(5)
        278.15
    """
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) + decimal.Decimal('273.15'))
    return float(convert)


def convertCelsiusToFahrenheit(degrees):
    """Converting Celsium measurment to Fahrenheit.
    Args:
        degrees(int, float): number of degrees to convert
    Returns:
        conversion
    Example:
        >>> convertCelsiusToFahrenheit(5)
        41
    """
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) / decimal.Decimal('5') * 9) + 32
    return float(convert)


def convertFahrenheitToCelsius(degrees):
    """Converting Fahrenheit measurment to Celsium.
    Args:
        degrees(int, float): number of degrees to convert
    Returns:
        conversion
    Example:
        >>> convertFahrenheitToCelsius(50)
        10.0
    """
    degrees = str(degrees)
    convert = ((decimal.Decimal(degrees) - 32) * 5) / decimal.Decimal('9')
    return float(convert)


def convertFahrenheitToKelvin(degrees):
    """Converting Fahrenheit measurment to Kelvin.
    Args:
        degrees(int, float): number of degrees to convert
    Returns:
        conversion
    Example:
        >>> convertFahrenheitToKelvin(50)
        283.15
    """
    degrees = str(degrees)
    convert = (((decimal.Decimal(degrees) + decimal.Decimal('459.67')) * 5) /
               decimal.Decimal('9'))
    return float(convert)


def convertKelvinToCelsius(degrees):
    """Converting Kelvin measurment to Celsius.
    Args:
        degrees(int, float): number of degrees to convert
    Returns:
        conversion
    Example:
        >>> convertKelvinToCelsius(500)
        226.85
    """
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) - decimal.Decimal('273.15'))
    return float(convert)


def convertKelvinToFahrenheit(degrees):
    """Converting Kelvin measurment to Fahrenheit.
    Args:
        degrees(int, float): number of degrees to convert
    Returns:
        conversion
    Example:
        >>> convertKelvinToFahrenheit(500)
        440.33
    """
    degrees = str(degrees)
    convert = (((decimal.Decimal(degrees) * 9) / decimal.Decimal('5'))
               - decimal.Decimal('459.67'))
    return float(convert)
