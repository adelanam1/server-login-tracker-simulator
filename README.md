# Server Login Tracker Simulator

This project is a simple Server Login Tracker Simulator designed to demonstrate basic Python skills for tracking and auditing login activity. It processes login data from a CSV file, formats it into a readable table, and exports the results to a text file.

## Features

- Parses login activity from a CSV file
- Formats data into a clear, readable format
- Automatically exports the table to a `.txt` file
- Demonstrates beginner-level Python skills with Pandas

## How It Works

1. **Data Input**: The program reads a CSV file containing sample login records.
2. **Data Processing**: It uses Python's Pandas library to clean and format the data.
3. **Output**: The program prints the login activity in a readable format and saves it to `login_audit_report.txt`.

## Sample CSV Structure

```csv
User_ID,Username,Login_Time,Logout_Time,IP_Address,File_Accessed
101,jdoe,2024-02-10 08:23:45,2024-02-10 12:45:30,192.168.1.10,Client_Info.xlsx
102,asmith,2024-02-10 09:15:10,2024-02-10 14:05:45,192.168.1.11,Sales_Report.pdf
```

## Example Output

```plaintext
User_ID: 101
Username: jdoe
Login_Time: 2024-02-10 08:23:45
Logout_Time: 2024-02-10 12:45:30
IP_Address: 192.168.1.10
File_Accessed: Client_Info.xlsx

User_ID: 102
Username: asmith
Login_Time: 2024-02-10 09:15:10
Logout_Time: 2024-02-10 14:05:45
IP_Address: 192.168.1.11
File_Accessed: Sales_Report.pdf

Report successfully exported to 'login_audit_report.txt'
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/server-login-tracker.git
cd server-login-tracker
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Program

```bash
python main.py
```

The login activity report will be printed to the console and saved as `login_audit_report.txt`.

## Requirements

- Python 3.x
- pandas==2.0.3

## License

This project is open-source and intended for educational purposes only.
