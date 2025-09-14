
# Data Filtering System

## Overview

The Data Filtering System is a Python-based project designed to validate, filter, and process records containing different types of structured data. It ensures that all data fields (such as phone numbers, national identification numbers, dates, geographic coordinates, and monetary values) comply with strict predefined formats.

The project was developed as part of the course **Autómatas y Lenguajes Formales** at the University of Murcia.

---

## Features

* Validation of:

  * Phone numbers (Spanish and international formats).
  * NIF (Spanish National Identification Number), including foreign formats.
  * Dates and times, supporting multiple formats.
  * Geographic coordinates in decimal, sexagesimal, and GPS compact formats.
  * Monetary values in euros.
* Data filtering by:

  * Phone number.
  * NIF.
  * Time interval.
  * Location radius.
* Conversion functions between supported formats (e.g., decimal coordinates to GPS format).
* Error handling and input validation to ensure only valid data is processed.

---

## Getting Started

### Requirements

* Python **3.12** or higher.
* No external dependencies (only Python standard library is used).

### Installation

Clone the repository:

```bash
git clone https://github.com/Enrikkk/Data-Filtering-System.git
cd Data-Filtering-System/code
```

### Run the program

```bash
python3 main.py <option> <arguments>
```

---

## Usage

The program is executed from the command line.

### Commands

* **Filter by phone number**

  ```bash
  python3 main.py -sphone <phone_number> <input_file>
  ```

* **Filter by NIF**

  ```bash
  python3 main.py -snif <nif> <input_file>
  ```

* **Filter by time interval**

  ```bash
  python3 main.py -stime <start_time> <end_time> <input_file>
  ```

* **Filter by location (radius in km)**

  ```bash
  python3 main.py -slocation <coordinates> <radius> <input_file>
  ```

* **Normalize and print all valid records**

  ```bash
  python3 main.py -n <input_file>
  ```

---

## Supported Formats

### Phone Numbers

* Simplified 9-digit Spanish numbers.

  ```
  666777999
  666 777 999
  ```
* International format similar to **E.164**, with spaces allowed between groups.

  ```
  +34 666 777 999
  +1 123 6666 77 9999
  ```

### NIF

* Standard Spanish format: 8 digits followed by a control letter.
  Example: `12345678Z`
* Foreign format: starting with X, Y, or Z, followed by 7 digits and a control letter.
  Example: `X1234567L`

### Dates and Times

* Format 1: `YYYY-MM-DD HH:MM`
  Example: `1945-08-06 08:15`
* Format 2: `Month DD, YYYY HH:MM AM/PM`
  Example: `August 6, 1945 8:15 AM`
* Format 3: `HH:MM:SS DD/MM/YYYY`
  Example: `08:15:00 06/08/1945`

### Coordinates

* Decimal:

  ```
  30.0, -40.5
  -25.05, +15.123
  ```
* Sexagesimal:

  ```
  30° 0' 0.0000" N, 40° 30' 0.0000" W
  25° 3' 0.0000" S, 15° 7' 22.8000" E
  ```
* GPS compact:

  ```
  0300000.0000N0403000.0000W
  0250300.0000S0150722.8000E
  ```

### Monetary Values

* Amounts expressed in euros, with optional decimals.

  ```
  50€
  2312.5€
  ```

---

## Example

### Input File (`example.txt`)

```
666 777 999 ; 12345678Z ; 1945-08-06 08:15 ; 30.0, -40.5 ; Laptop ; 2312.5€
+34 666 777 999 ; 12345678Z ; August 6, 1945 8:15 AM ; 0300000.0000N0403000.0000W ; Laptop ; 2312.5€
777 888 999 ; 12345678Z ; 1945-13-06 08:15 ; 95.0, 200.0 ; Laptop ; 2312.5€
```

### Command

```bash
python3 main.py -sphone "+34 666 777 999" example.txt
```

### Filtered Output

```
+34 666 777 999 ; 12345678Z ; August 6, 1945 8:15 AM ; 0300000.0000N0403000.0000W ; Laptop ; 2312.5€
```

> Note: The third line is discarded because it contains an invalid date and out-of-range coordinates.
> Additional test files are available in the `/code/tests/` directory.

---

## Error Handling

The system validates all fields before processing. If any field is invalid, the record is discarded, and appropriate error messages are shown (for example, malformed dates, incorrect NIF control letters, or out-of-range coordinates).

---

## Project Structure

```
├── code/
│   ├── main.py                  # Main program file
│   ├── tests/                   # Test input files for validation and filtering
├── README.md                    # Project documentation
├── ALF - Boletín de Prácticas 2024-25.pdf   # Practice description (course document)
```

---

## Acknowledgments

This project was developed as part of the **Autómatas y Lenguajes Formales** course at the **University of Murcia**.


