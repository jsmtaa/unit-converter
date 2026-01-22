# Unit Converter

A lightweight Python project that converts **single unit values** using a unit registry and returns results in multiple numeric formats.

This project is intentionally minimal and focused on correctness and formatting rather than features.

## Description

The Unit Converter allows conversion between compatible units (e.g. meters to kilometers) and formats the result in one of three modes:

* Numeric
* Exponential notation
* Scientific notation

It uses **Pint’s `UnitRegistry`** to handle unit definitions and conversions reliably.

## Features

* Single-value unit conversion
* Uses a unit registry for correctness
* Multiple output formats

## Requirements

* Python 3.x
* Pint (unit registry)

## Installation

Clone the repository and install the required dependency:

```bash
git clone https://github.com/your-username/unit-converter.git
cd unit-converter
pip install pint
```

## Usage

Basic conversion:

```python
convert(value, to_unit, from_unit)
```

With formatting modes:

```python
convert(value, to_unit, from_unit, mode="numeric")
convert(value, to_unit, from_unit, mode="exponential")
convert(value, to_unit, from_unit, mode="scientific")
```

## Output Modes

* **Numeric**
  `1000.0 units`

* **Exponential notation**
  `1.00e+03 units`

* **Scientific notation**
  `1.00 x 10³ units`

## Project Structure

## Limitations

* Converts only **one value at a time**
* No batch conversions
* No CLI or GUI
* Formatting options are limited
* Unit support depends on Pint

## Purpose

This project is mainly intended for:

* Learning unit conversion logic
* Practicing clean Python design
* Exploring numeric formatting (scientific vs exponential)
* Building a small, focused repository

## Future Improvements

* Batch conversions
* Command-line interface
* More formatting controls
* Error handling improvements

## License

MIT License
