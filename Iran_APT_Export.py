import os
import subprocess
import urllib3
from pymisp import PyMISP

# Suppress the insecure request warnings for local IP
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

misp_url = 'https://192.168.0.60'

# SECURE CHANGE 1: Fetch the API key from an environment variable
misp_key = os.environ.get('MISP_API_KEY')

if not misp_key:
    print("Error: MISP_API_KEY environment variable is not set.")
    exit(1)

# Initialize PyMISP
misp = PyMISP(misp_url, misp_key, False)

# List of known Iranian threat actors using wildcards
iranian_apts = [
    "%APT33%", "%APT34%", "%APT35%", "%APT39%", 
    "%MuddyWater%", "%OilRig%", "%Charming Kitten%", 
    "%Agrius%", "%Pioneer Kitten%", "%Handala%", 
    "%CyberAv3ngers%", "%Void Manticore%"
]

print("Searching MISP for Iranian APT indicators using the search API...")

# In newer PyMISP versions, 'search' replaces 'restSearch'
response = misp.search(controller='attributes', return_format='csv', tags=iranian_apts)

# SECURE CHANGE 2: Ensure we write the CSV to the correct Git directory
os.chdir('/opt/misp-digest-repo/')

with open('iran_iocs.csv', 'w') as f:
    f.write(str(response))

print("Export complete! Check the iran_iocs.csv file.")

print("Pushing updates to GitHub via SSH...")
subprocess.run(["git", "add", "iran_iocs.csv"])
subprocess.run(["git", "commit", "-m", "Auto-update Iranian APT IOCs"])
subprocess.run(["git", "push", "origin", "main"])
