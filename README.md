# Script to migrate Passwords from TPM Password manager to lastpass.

Steps to follow.
1. Export all the passwords from the TPM tool into a CSV file. Refer - https://teampasswordmanager.com/docs/export_import/
2. Download the lastpass cli tool. Refer - https://github.com/lastpass/lastpass-cli
3. login to the account using cli. "lpass login <username>"
4. Run the script after updating the path to the CSV file and also the folder on lastpass under which passwords need to be synced.
