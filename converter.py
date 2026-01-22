from pint import UnitRegistry

ureg = UnitRegistry()

def main():
    # Values are taken from here
    value, from_unit, to_unit = 1, "m", "km"
    
    converted = convert(value, from_unit, to_unit)

    print("Converted:", converted)
    print("Exponential:", format_exponential(converted.magnitude))
    print("Scientific:", format_scientific(converted.magnitude))


# Main conversion logic
def convert(value, from_unit, to_unit, mode="numeric"):
    converted = float(value) * ureg.__call__(from_unit).to(ureg.__call__(to_unit))

    match mode:
        case "numeric":
            return converted
        case "exponential":
            return format_exponential(converted.magnitude)
        case "scientific":
            return format_scientific(converted.magnitude)


# Exponential Notation
def format_exponential(value):
    return f"{value:.2e}"


# Scientific Notation
def format_scientific(value):
    # The decimal places or the exponent value can be derived from its base numeric value
    # For simplicity, I just used format_exponential() and split 'e' which takes the exponent from value[1]
    value = format_exponential(value).split('e')
    base, exponent = value[0], value[1]
    sign = exponent[0]

    # Check exponent after sign (happens because format_exponential() returns 00 when there aren't any exponents)
    if exponent[1:] == "00":
        exponent = exponent[1:].removeprefix("00")
    # Check if exponent (after sign) has leading zero (e.g. 01, 02, 03)
    elif exponent[1] == "0":
        exponent = exponent[0] + exponent[2:]

    # Remove positive sign if positive (usual format conventions)
    if sign == "+":
        exponent = exponent.removeprefix('+')

    sup = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
    exponent = str(exponent).translate(sup)

    return f"{base} x 10{exponent}"


if __name__ == "__main__":
    main()