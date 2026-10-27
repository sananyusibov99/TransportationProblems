# Transportation Problem (interface prototype)

The interface for a program that solves the transportation problem from operations research. Made in April 2021 as part of the Data Science master's programme at UFAZ.

## What is done

- The program asks for the number of sources and destinations, then builds a cost table of that size
- Sources are labelled with Roman numerals and destinations with letters
- Supply and demand fields for each row and column
- A live comparison of total supply and total demand, to check whether the problem is balanced
- Placeholders for the results of three methods for finding an initial solution: North-West Corner, Least Cost Cell and Vogel's Approximation

## Status

This is version 1.0 of the interface only. The **Calculate** button does nothing yet, because the solution methods were never implemented.

## Tech stack

Python, Tkinter

## How to run

```bash
python main.py
```

Enter the number of destinations and sources in the console, and the table window opens.
