from pint import UnitRegistry

ureg = UnitRegistry()

def main():
    value = 1
    from_unit = "m"
    to_unit = "km"
    converted = convert(value, from_unit, to_unit)

    print("Converted:", converted, to_unit)
    print("Exponential:", format_exponential(converted))
    print("Scientific:", format_scientific(converted))


# Simple conversion
def convert(value, from_unit, to_unit):
    return float(value) * ureg.__call__(from_unit).to(ureg.__call__(to_unit)).magnitude

"""
Default formatting:
    format_scientific if len < 0 or len > 3 because 123.0 is unecessary for 1.23 x 10^1
    format_exponential if not satisfied
"""

# Scientific
def format_scientific(value):
    value = format_exponential(value).split('e')
    base, exponent = value[0], value[1]
    sign = exponent[0]

    # Check if exponent (after sign) is 00
    if exponent[1:] == "00":
        exponent = exponent[1:].removeprefix("00")
    # Check if exponent (after sign) has leading zero
    elif exponent[1] == "0":
        exponent = exponent[0] + exponent[2:]

    # Remove positive sign if positive
    if sign == "+":
        exponent = exponent.removeprefix('+')

    sup = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
    exponent = str(exponent).translate(sup)

    return f"{base} x 10{exponent}"

# Exponential
def format_exponential(value):
    return f"{value:.2e}"

if __name__ == "__main__":
    main()