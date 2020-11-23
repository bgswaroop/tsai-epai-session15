from collections import namedtuple
from datetime import datetime
from itertools import islice

Ticket = namedtuple('Ticket', 'summons_number, plate_id, registration_state, plate_type, issue_date, violation_code, '
                              'vehicle_body_type, vehicle_make, violation_description')
date_formatter = lambda x: datetime.strptime(x, '%m/%d/%Y')
ticket_datatype = [int, str, str, str, date_formatter, int, str, str, str]


def fetch_data():
    """
    Goal 1
    Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate
    - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer,
    then it should be stored as an integer, etc.
    :return: generator that returns single ticket at a time
    """
    with open('nyc_parking_tickets_extract.csv', 'r') as f:
        next(f)
        for line in f:
            line_data = [x.strip() for x in line.strip().split(',')]
            line_data = [item_type(item) for item, item_type in zip(line_data, ticket_datatype)]
            yield Ticket(*line_data)
    return 'Finished reading the file'


def compute_violations_by_car_make():
    """
    Goal 2
    Calculate the number of violations by car make.
    :return: A dictionary containing the violations per car make
    """
    parking_tickets = fetch_data()
    violations = {}
    for ticket in parking_tickets:
        if ticket.vehicle_make in violations:
            violations[ticket.vehicle_make] += 1
        else:
            violations[ticket.vehicle_make] = 1
    return violations


def print_data():
    """
    Print the entire data
    :return:
    """
    parking_tickets = fetch_data()
    for ticket in islice(parking_tickets, 10000):
        print(ticket)


if __name__ == '__main__':
    print_data()
    print(compute_violations_by_car_make())