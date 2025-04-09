# global-space-missions-analysis

This project involves analyzing a dataset of fictional global space missions from the years 1970 to 1999. 
The goal is to filter and analyze the missions based on various criteria, 
such as prime years, divisibility by specific numbers, mission type, success status, and more. 
This is done using a Python script that reads the data, processes it, 
and outputs the filtered results based on command-line arguments.

## Features

- **Read Data**: The project reads a CSV dataset containing space missions from 1970 to 1999.
- **Filter by Prime Year**: The script can filter missions based on whether the year is prime.
- **Filter by Divisibility**: Filter missions for years divisible by a specific number.
- **Additional Filters**: You can extend the filtering capabilities for mission type, country, or success status.
- **Command-Line Interface (CLI)**: Use various arguments to filter the dataset as per your needs.

## Requirements

- Python 3.x
- `argparse` for command-line parsing
- `pytest` for unit testing

### Install Dependencies

Before running the script, install the required dependencies using the following command:

```bash
pip install -r requirements.txt
