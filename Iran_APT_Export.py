import urllib3
from pymisp import PyMISP

# Suppress the insecure request warnings for local IP
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Replace with your actual MISP API key
misp_url = 'https://192.168.0.60'


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
# We specify controller='attributes' to get the individual IOCs
response = misp.search(controller='attributes', return_format='csv', tags=iranian_apts)

# The response from search() is often a string when CSV is requested
with open('iran_iocs.csv', 'w') as f:
    f.write(str(response))

print("Export complete! Check the iran_iocs.csv file in your directory.")
