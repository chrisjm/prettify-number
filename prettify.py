def number(n):
    """
    Return a prettified number, either integer or float.

    Parameters
    ----------
    n : int or float
        number to prettify

    Returns
    -------
    str
        Prettified string
    """

    ONE_MILLION = 1000000
    ONE_BILLION = ONE_MILLION * 1000
    ONE_TRILLION = ONE_BILLION * 1000

    # Ensure input is proper format
    if not isinstance(n, (int, float)):
        raise TypeError('input format should be an integer or float')

    # Ensure input is in range
    if n >= ONE_TRILLION * 1000:
        raise ValueError('input must be less than a quadrillion')

    # Format numbers under 1M with a comma
    if n < ONE_MILLION:
        return f'{n:,}'

    # Determine arguments for prettifying
    if n >= ONE_MILLION and n < ONE_BILLION:
        scale = ONE_MILLION
        suffix = "M"
    elif n >= ONE_BILLION and n < ONE_TRILLION:
        scale = ONE_BILLION
        suffix = "B"
    else:
        scale = ONE_TRILLION
        suffix = "T"

    # Get shorthand number by dividing by the scale
    shorthand = n / scale

    # Determine if prettified number needs a decimal (e.g. 1.0 -> 1)
    if shorthand % 1 == 0:
        shorthand = int(shorthand)
    else:
        shorthand = f'{shorthand:.1f}'

    return str(shorthand) + suffix
