import pandas as pd
from datetime import datetime

data = pd.read_csv('client_server_data_updated.csv')

failed_logins = data[data['Status'] == 'Failed']
successful_logins = data[(data['Status'] == 'Success') & (data['Action'] == 'Login')]
file_access = data[data['Action'] == 'Accessed']
suspicious_activity = failed_logins.groupby('IP_Address').filter(lambda x: len(x) > 1)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = []
report.append(f"==== CLIENT SERVER AUDIT REPORT ====")
report.append(f"Generated on: {timestamp}\n")

if not failed_logins.empty:
    report.append("**Failed Logins:**\n")
    report.append(failed_logins.to_string(index=False))
else:
    report.append("No failed login attempts found.\n")

if not successful_logins.empty:
    report.append("\n**Successful Logins:**\n")
    report.append(successful_logins.to_string(index=False))
else:
    report.append("\nNo successful logins found.\n")

if not file_access.empty:
    report.append("\n**File Access Logs:**\n")
    report.append(file_access.to_string(index=False))
else:
    report.append("\nNo file access logs found.\n")

if not suspicious_activity.empty:
    report.append("\n**Suspicious Activity (Multiple Failed Logins):**\n")
    report.append(suspicious_activity.to_string(index=False))
else:
    report.append("\nNo suspicious activity detected.\n")

report.append("\n==== END OF REPORT ====")

output_filename = f"/Users/yourusername/Desktop/Client_Server_Audit_Project/audit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(output_filename, 'w') as file:
    file.write("\n".join(report))

print(f"Audit report saved as {output_filename}")
