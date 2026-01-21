from pint import UnitRegistry

ureg = UnitRegistry()

def main():
    converted = convert(1, "m", "km")
    print(format_scientific(converted))

# Simple conversion
def convert(value, from_unit, to_unit):
    return float(value) * ureg.__call__(from_unit).to(ureg.__call__(to_unit)).magnitude

# Exponential
def format_exponential(value):
    return f"{value:.1e}"

if __name__ == "__main__":
    main()