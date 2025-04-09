import pytest
from src.analyze_space_missions import is_prime, is_divisible, filter_data

# Sample data for tests (matches the contents of global_space_missions.csv)
sample_data = [
    {'Mission Name': 'Mission_1', 'Year': '1989', 'Mission Type': 'unmanned', 'Destination': 'Asteroids', 'Successful?': 'False', 'Lead Agency': 'NASA', 'Country of Origin': 'USA'},
    {'Mission Name': 'Mission_2', 'Year': '1973', 'Mission Type': 'manned',   'Destination': 'Mars',      'Successful?': 'True',  'Lead Agency': 'Virgin Galactic', 'Country of Origin': 'Russia'},
    {'Mission Name': 'Mission_3', 'Year': '1989', 'Mission Type': 'unmanned', 'Destination': 'Moon',      'Successful?': 'True',  'Lead Agency': 'NASA', 'Country of Origin': 'Europe'},
]

# Tests for is_prime function
def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(1973) is True
    assert is_prime(1989) is False

# Tests for is_divisible function
def test_is_divisible():
    assert is_divisible(1989, 3) is True   # 1989 is divisible by 3
    assert is_divisible(1973, 3) is False

# Test filtering for prime years
def test_filter_data_prime():
    result = filter_data(sample_data, prime=True)
    # Only Mission_2 (1973) is prime
    assert len(result) == 1
    assert result[0]['Mission Name'] == 'Mission_2'

# Test filtering for years divisible by a given integer
def test_filter_data_divisible():
    result = filter_data(sample_data, divisible_by=3)
    # Mission_1 and Mission_3 (1989) are divisible by 3
    assert len(result) == 2
    mission_names = [row['Mission Name'] for row in result]
    assert 'Mission_1' in mission_names
    assert 'Mission_3' in mission_names

# Test filtering for missions that succeeded
def test_filter_data_success():
    result = filter_data(sample_data, success=True)
    # Mission_2 and Mission_3 are successful
    assert len(result) == 2
    for row in result:
        assert row['Successful?'].strip().lower() == "true"

# Test filtering for missions that failed
def test_filter_data_failure():
    result = filter_data(sample_data, failure=True)
    # Only Mission_1 failed
    assert len(result) == 1
    assert result[0]['Successful?'].strip().lower() == "false"

# Test filtering by manned missions
def test_filter_data_manned():
    result = filter_data(sample_data, manned=True)
    # Only Mission_2 is manned
    assert len(result) == 1
    assert result[0]['Mission Type'].strip().lower() == "manned"

# Test filtering by unmanned missions
def test_filter_data_unmanned():
    result = filter_data(sample_data, unmanned=True)
    # Mission_1 and Mission_3 are unmanned
    assert len(result) == 2
    for row in result:
        assert row['Mission Type'].strip().lower() == "unmanned"

# Test filtering by country
def test_filter_data_country():
    result = filter_data(sample_data, country="USA")
    # Only Mission_1 is from USA
    assert len(result) == 1
    assert result[0]['Country of Origin'].strip().lower() == "usa"

# Combined filter test: prime and divisible_by both applied
def test_filter_data_combined():
    result = filter_data(sample_data, prime=True, divisible_by=3, success=True)
    # prime filter -> only Mission_2 is prime, but 1973 is not divisible by 3 so result should be empty.
    assert len(result) == 0
