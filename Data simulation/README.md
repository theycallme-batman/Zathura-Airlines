# Flight Data Tables

This README provides an overview of the structure and schema of the flight data tables generated from the script stimulating flight data.

## Table Structure

### Table: flights
| Column Name            | Data Type                 | Description                                       |
|------------------------|---------------------------|---------------------------------------------------|
| id                     | bigint                    | Unique identifier for each flight                 |
| flight_code            | text                      | Flight code                                        |
| source_airport         | text                      | Source airport code                               |
| destination_airport    | text                      | Destination airport code                          |
| source_city            | text                      | Source city                                       |
| destination_city       | text                      | Destination city                                  |
| estimated_departure_time | timestamp without time zone | Estimated departure time                        |
| departure_time         | text                      | Actual departure time                             |
| estimated_arrival_time | timestamp without time zone | Estimated arrival time                          |
| arrival_time           | text                      | Actual arrival time                               |
| passenger_data         | text (array of JSON)     | Array of JSON objects containing passenger data   |
| total_passengers       | bigint                    | Total number of passengers on the flight          |
| status                 | text                      | Flight status                                     |
| load_timestamp         | timestamp without time zone | Timestamp of data loading                        |

### Table: airplanes
| Column Name            | Data Type                 | Description                                       |
|------------------------|---------------------------|---------------------------------------------------|
| airplane_id            | text                      | Unique identifier for each airplane               |
| name                   | text                      | Name of the airplane                              |
| type                   | text                      | Type of airplane                                  |
| total_seats            | bigint                    | Total number of seats in the airplane             |
| classes                | text                      | Classes available in the airplane                 |
| fuel_capacity          | text                      | Fuel capacity of the airplane                      |
| range                  | text                      | Range of the airplane                             |
| load_timestamp         | timestamp without time zone | Timestamp of data loading                        |

### Table: flight_schedules
| Column Name            | Data Type                 | Description                                       |
|------------------------|---------------------------|---------------------------------------------------|
| name                   | text                      | Name of the flight schedule                        |
| frequency              | text                      | Frequency of the flight schedule                   |
| source                 | text                      | Source airport code                               |
| destination            | text                      | Destination airport code                          |
| timings                | text                      | Timings of the flight schedule                     |
| load_timestamp         | timestamp without time zone | Timestamp of data loading                        |

### Table: payments
| Column Name            | Data Type                 | Description                                       |
|------------------------|---------------------------|---------------------------------------------------|
| flight_id              | bigint                    | Unique identifier for each flight                  |
| first_name             | text                      | First name of the passenger                       |
| last_name              | text                      | Last name of the passenger                        |
| contact_number         | text                      | Contact number of the passenger                    |
| email_id               | text                      | Email ID of the passenger                          |
| seat_number            | text                      | Seat number booked by the passenger               |
| mode_of_payment        | text                      | Mode of payment for the booking                    |
| time_of_payment        | timestamp without time zone | Time of payment                                 |
| amount                 | numeric(20,2)             | Amount paid for the booking                        |
| transaction_id         | bigint                    | Unique identifier for each transaction            |
| agent                  | text                      | Agent who processed the payment                   |
| load_timestamp         | timestamp without time zone | Timestamp of data loading                        |

