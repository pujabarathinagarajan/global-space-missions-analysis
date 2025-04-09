import csv
import argparse
from math import sqrt

# Step 1: Function to read data from CSV
def read_data(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Step 2: Function to check if a number is prime
def is_prime(year):
    if year < 2:
        return False
    for i in range(2, int(sqrt(year)) + 1):
        if year % i == 0:
            return False
    return True

# Step 3: Function to check if year is divisible by a given integer
def is_divisible(year, divisor):
    return year % divisor == 0

# Step 4: Filter data based on conditions, including new filters
def filter_data(data, prime=False, divisible_by=None, success=False, failure=False,
                agency=None, destination=None, country=None, manned=False, unmanned=False):
    filtered_data = []

    for row in data:
        try:
            year = int(row['Year'])
        except ValueError:
            continue  # Skip rows with invalid year values

        # Existing filters:
        if prime and not is_prime(year):
            continue
        if divisible_by is not None and not is_divisible(year, divisible_by):
            continue
        if agency and row.get('Lead Agency', '').strip().lower() != agency.lower():
            continue
        if destination and row.get('Destination', '').strip().lower() != destination.lower():
            continue

        # New filters:
        if success and row.get('Successful?', '').strip().lower() != 'true':
            continue
        if failure and row.get('Successful?', '').strip().lower() != 'false':
            continue
        if manned and row.get('Mission Type', '').strip().lower() != 'manned':
            continue
        if unmanned and row.get('Mission Type', '').strip().lower() != 'unmanned':
            continue
        if country and row.get('Country of Origin', '').strip().lower() != country.lower():
            continue

        filtered_data.append(row)
    return filtered_data

# Step 5: Print the filtered data
def print_data(data):
    for row in data:
        print(row)

# Step 6: Command-Line Interface Setup with additional arguments
def main():
    parser = argparse.ArgumentParser(description='Analyze space mission data')
    parser.add_argument('file', help='Path to the CSV file')
    parser.add_argument('-p', action='store_true', help='Filter for prime years')
    parser.add_argument('-a', type=int, help='Filter for years divisible by this number')
    parser.add_argument('--agency', type=str, help='Filter for missions led by the specified agency')
    parser.add_argument('--destination', type=str, help='Filter for missions with the specified destination')

    # New command-line flags:
    parser.add_argument('--success', action='store_true', help='Filter for missions that succeeded')
    parser.add_argument('--failure', action='store_true', help='Filter for missions that failed')
    parser.add_argument('--manned', action='store_true', help='Filter for manned missions')
    parser.add_argument('--unmanned', action='store_true', help='Filter for unmanned missions')
    parser.add_argument('--country', '-c', type=str, help='Filter by country (Country of Origin)')

    args = parser.parse_args()

    # Step 7: Read data from the file
    data = read_data(args.file)

    # Step 8: Filter data based on provided conditions
    filtered_data = filter_data(
        data,
        prime=args.p,
        divisible_by=args.a,
        success=args.success,
        failure=args.failure,
        agency=args.agency,
        destination=args.destination,
        country=args.country,
        manned=args.manned,
        unmanned=args.unmanned,
    )

    # Step 9: Print the results
    print_data(filtered_data)

if __name__ == '__main__':
    main()
