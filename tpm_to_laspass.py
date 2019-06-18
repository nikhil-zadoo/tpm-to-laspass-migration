import csv
import subprocess
import time

path = "Update the Path to CSV file exported from TPM password manager"
with open(path, newline='') as csvfile:
    reader = csv.DictReader(csvfile, escapechar='\\')
    for row in reader:
        command = 'printf "Username: ' + row['Username'].replace('"', '\\"').replace("%", "%%") \
        + '\nPassword: ' + row['Password'].replace('"', '\\"').replace("%", "%%") \
        + '\nURL: ' + row['Access information'].replace('"', '\\"').replace("%", "%%") \
        + '\nNotes: ' + row['Notes'].replace('"', '\\"').replace("%", "%%") \
        + '" | lpass add Shared-migrated-from-TPM/' \
        + row['Name'].replace(" ", "-").replace("(", "-").replace(")", "-").replace('"', '') \
        + ' --non-interactive --sync=now'
        
        output = subprocess.check_output(command, shell=True)
        time.sleep(5)
