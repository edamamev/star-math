import math

# Most of this math for this script came from the Wonderful Artifexian
# and his Patrons 
# He can be found here: https://www.youtube.com/c/Artifexian
# The math document can be found here:
# https://docs.google.com/spreadsheets/d/1AML0mIQcWDrrEHj-InXoYsV_QlhlFVuUalE3o-TwQco/copy
# 
# The rest of the math came from OmniCalculator
# Szyk, B. Luminosity Calculator. Available at:
# https://www.omnicalculator.com/physics/luminosity.
# Accessed: Mar 07, 2025.

SUN_TEMPERATURE = 5778
ZERO_POINT_LUMINOSITY = int(3.0128 * pow(10, 13))
SOLAR_LUMINOSITY = int(3.828 * pow(10, 11))

COLOUR_O = (155, 176, 255)
COLOUR_B = (170, 191, 255)
COLOUR_A = (202, 215, 255)
COLOUR_F = (248, 247, 255)
COLOUR_G = (255, 244, 234)
COLOUR_K = (255, 210, 161)
COLOUR_M = (255, 204, 111)


def get_star_luminosity(star_mass: float):
    """
    Returns a Star's Luminosity in Solar Luminosities.
    Requires the Star's Mass in Solar Masses.
    """
    if (star_mass < 0.43):
        return 0.23 * pow(star_mass, 2.3)
    elif (star_mass < 2):
        return pow(star_mass, 4)
    else:
        return 1.4 * pow(star_mass, 3.5)


def get_star_luminosity_2(star_radius: float, star_temperature: float):
    """
    Returns a Star's Luminosity in Solar Luminosities.
    Requires the Star's Radius in Solar Radii and its Temperature in
    Kelvin.
    """
    return pow(star_radius, 2) * pow(star_temperature / SUN_TEMPERATURE, 4)


def get_maximum_star_age(star_mass: float, star_luminosity: float):
    """
    Returns a Star's Maximum Life in Billions of Years.
    Requires the Star's Mass in Solar Masses and it's Luminosity in Solar
    Luminosities
    """
    return 10 * (star_mass / star_luminosity)


def get_star_radius(star_mass: float):
    """
    Returns a Star's Radius in Solar Radii.
    Requires the Star's Mass in Solar Masses.
    """
    if (star_mass < 1):
        return pow(star_mass, 0.8)
    else:
        return pow(star_mass, 0.57)


def get_star_density(star_mass: float, star_radius: float):
    """
    Returns a Star's Density in Solar Density's
    """
    return star_mass / pow(star_radius, 2)


def get_star_temperature(star_luminosity: float, star_radius: float):
    """
    Returns a Star's Temperature in Kelvin.
    Requires the Star's Luminosity in Solar Luminosities, and it's Radius in
    Solar Radii
    """
    return 5776 * pow((star_luminosity / pow(star_radius, 2)), 0.25)


def get_star_colour(star_temperature: float):
    """
    Returns a Star's Colour in RGB.
    Requires the Star's Temperature in Kelvin.
    """
    min_temp = 0
    max_temp = 0
    colour_min = (0,0,0)
    colour_max = (0,0,0)

    if (star_temperature <= 3700):
        min_temp = 0
        max_temp = 3700
        colour_max = COLOUR_M
    elif (star_temperature > 3700 and star_temperature <= 5200):
        min_temp = 3700
        max_temp = 5200
        colour_min = COLOUR_M
        colour_max = COLOUR_K
    elif (star_temperature > 5200 and star_temperature <= 6000):
        min_temp = 5200
        max_temp = 6000
        colour_min = COLOUR_K
        colour_max = COLOUR_G
    elif (star_temperature > 6000 and star_temperature <= 7500):
        min_temp = 6000
        max_temp = 7500
        colour_min = COLOUR_G
        colour_max = COLOUR_F
    elif (star_temperature > 7500 and star_temperature <= 10000):
        min_temp = 7500
        max_temp = 10000
        colour_min = COLOUR_F
        colour_max = COLOUR_A
    elif (star_temperature > 10000 and star_temperature <= 33000):
        min_temp = 10000
        max_temp = 33000
        colour_min = COLOUR_A
        colour_max = COLOUR_O
    else:
        return COLOUR_O
    temp_ratio = (star_temperature - min_temp) / (max_temp - min_temp)
    colour_0 = colour_min[0] + int((colour_max[0] - colour_min[0]) * temp_ratio)
    colour_1 = colour_min[1] + int((colour_max[1] - colour_min[1]) * temp_ratio)
    colour_2 = colour_min[2] + int((colour_max[2] - colour_min[2]) * temp_ratio)
    return (colour_0, colour_1, colour_2)


def get_star_habitable_zone(star_luminosity: float):
    """
    Returns a Star's Habitable Zone in Astronomic Units.
    Requires the Star's Luminosity in Solar Luminosities.
    """
    return (pow(star_luminosity / 1.1, 0.5),pow(star_luminosity / 0.53, 0.5))


def get_star_life_possibility(star_mass: float, star_current_age: float):
    """
    Returns a Star's possiblity of having life within it's system.
    Requires the Star's Mass in Solar Masses and it's Current Age in Billions
    of Years
    """
    if (star_mass >= 0.5) and (star_mass <= 1.4):
        if (star_current_age >= 3.5):
            return "Life Possible"
        else:
            return "Star Too Young"
    else:
        return "Life Not Possible"


def get_star_luminosity_in_petawatts(star_luminosity):
    """
    Returns a Star's Luminosity in Petawatts.
    Requires the Star's Luminosity in Solar Luminosities.
    """
    return star_luminosity * SOLAR_LUMINOSITY


def get_star_absolute_magnitude(star_luminosity: float):
    """
    Returns a Star's Absolute Magnitude.
    Requires the Star's Luminosity in Solar Luminosities.
    """
    return -2.5 * math.log10( \
        get_star_luminosity_in_petawatts(star_luminosity), \
        ZERO_POINT_LUMINOSITY
        )


def get_star_apparent_magnitude( \
        star_absolute_magnitude: float, \
        star_distance_from_observer_parsecs: float):
    """
    Returns a Star's Apparent Magnitude.
    Requires the Star's Absolute Magnitude and it's Distance from the Observer
    in Parsecs
    """
    return star_absolute_magnitude \
        - 5 + 5 * math.log10(star_distance_from_observer_parsecs)
