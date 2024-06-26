# Security Log Report Generator

## Description

This project generates security reports based on system logs. The script reads logs from a CSV file, processes the data, and outputs a summary report of different event types.

## Technologies Used

- Python
- Pandas

## Prerequisites

- Python 3.x installed on your system
- Pandas library (can be installed via pip)

## Installation

1. Clone the repository or download the source code.

    ```bash
    git clone https://github.com/AC2002FR/Security-Log-Report-Generator
    cd security_log_report_generator
    ```

2. Install the required dependencies.

    ```bash
    pip install pandas
    ```

## Usage

1. Prepare your log file. For this example, we use a CSV file named `logs.csv` with the following format:

    ```csv
    timestamp,event_type,description
    2024-05-01 10:00:00,INFO,User logged in
    2024-05-01 10:05:00,WARNING,Disk space low
    2024-05-01 10:10:00,ERROR,Failed login attempt
    2024-05-01 10:15:00,INFO,User logged out
    ```

2. Run the script to generate the report.

    ```bash
    python generate_report.py
    ```

3. You should see an output like this:

    ```
    Security Log Report
    ===================
    Total Events: 4
    Info Events: 2
    Warning Events: 1
    Error Events: 1
    ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

Distributed under the MIT License. See `LICENSE` for more information.
