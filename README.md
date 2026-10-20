# Small Business Inventory Management System

A beginner-friendly, terminal-based Python mini-project for managing a small shop's stock and sales. It uses core Python concepts only—dictionaries, lists, loops, conditions, and arithmetic—and does not require external libraries.

## Features

- Add products with an ID, name, purchase price, selling price, current stock, and minimum stock level.
- View the complete product catalogue.
- Search for a product by ID.
- Add incoming stock.
- Record a sale and automatically reduce stock.
- Reject sales when the requested quantity exceeds available stock.
- Identify products at or below their minimum stock level.
- Calculate inventory value using purchase cost.
- Show sales, revenue, cost of goods sold, and gross profit for the current program session.

## Requirements

- Python 3.8 or newer recommended
- No external packages required

## How to run

Open a terminal in this folder and run:

```bash
python inventory_management.py
```

On some systems, use `python3` instead of `python`.

## Notes and limitations

- Product and sales data are held in memory, so they reset when the program exits.
- This is an educational console prototype, not a production point-of-sale system.
- Enter numeric values where prompted; the program validates common invalid inputs but is not intended to replace a full business application.

## Main Python concepts demonstrated

Variables, `input()` and `print()`, dictionaries, lists, `while` and `for` loops, conditional statements, and arithmetic operators.
