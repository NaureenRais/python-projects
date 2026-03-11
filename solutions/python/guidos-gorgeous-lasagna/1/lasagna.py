"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`
    """

    pass


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * PREPARATION_TIME
    

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return 2 * number_of_layers + elapsed_bake_time
# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calculate the remaining bake time in minutes.

    The lasagna has a fixed total bake time of 40 minutes. This function
    subtracts the elapsed baking time from the total to compute the
    remaining time.

    Args:
        elapsed_bake_time (int): The number of minutes the lasagna has been baking.

    Returns:
        int: The remaining bake time in minutes.
    """
    EXPECTED_BAKE_TIME = 40
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    Compute the preparation time in minutes for the given number of layers.

    Each lasagna layer takes 2 minutes to prepare.

    Args:
        number_of_layers (int): The number of lasagna layers being prepared.

    Returns:
        int: Total preparation time in minutes.
    """
    PREPARATION_TIME = 2
    return number_of_layers * PREPARATION_TIME
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Calculate the total elapsed cooking time in minutes.

    The total elapsed time is the sum of:
    - preparation time (2 minutes per layer), and
    - the already elapsed bake time.

    Formula:
        total = 2 * number_of_layers + elapsed_bake_time

    Args:
        number_of_layers (int): The number of lasagna layers.
        elapsed_bake_time (int): The elapsed baking time in minutes.

    Returns:
        int: Total time elapsed (in minutes) preparing and cooking.
    """
    return 2 * number_of_layers + elapsed_bake_time
    
