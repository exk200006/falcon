from falconpy import Intel

# Do not hardcode API credentials!
falcon = Intel(client_id="CLIENT_ID",
               client_secret="CLIENT_SECRET"
               )

response = falcon.query_report_entities(offset=integer,
                                        limit=integer,
                                        sort="string",
                                        filter="string",
                                        q="string",
                                        fields=["string", "string"]
                                        )

print(response)

//How to run this?

Client ID: 328bec5d654b4cbd95f55c7e8a474bdc
Client Secret: JK6r35ea2TIMQkEwLb74pAjx1qFvnHsRSh09m8zy


Falcon Wiki:
https://falconpy.io/Service-Collections/Intel.html#queryintelactorentities 
includes all API's

Falcon Install:https://falconpy.io/Usage/Installation-Upgrades-and-Removal.html

Crowdstrike github: https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/api_complete/_advanced.py


"""CrowdStrike FalconPy Quick Start."""
import os
from falconpy import Hosts

# Use the API Clients and Keys page within your Falcon console to generate credentials.
# You will need to assign the Hosts: READ scope to your client to run this example.

# CrowdStrike does not recommend you hardcode credentials within source code.
# Instead, provide these values as variables that are retrieved from the environment,
# read from an encrypted file or secrets store, provided at runtime, etc.
# This example retrieves credentials from the environment as the variables
# "FALCON_CLIENT_ID" and "FALCON_CLIENT_SECRET".

hosts = Hosts(client_id=os.getenv("FALCON_CLIENT_ID"),
              client_secret=os.getenv("FALCON_CLIENT_SECRET")
              )

SEARCH_FILTER = "hostname-search-string"

# Retrieve a list of hosts that have a hostname that matches our search filter
hosts_search_result = hosts.query_devices_by_filter(filter=f"hostname:*'*{SEARCH_FILTER}*'")

# Confirm we received a success response back from the CrowdStrike API
if hosts_search_result["status_code"] == 200:
    hosts_found = hosts_search_result["body"]["resources"]
    # Confirm our search produced results
    if hosts_found:
        # Retrieve the details for all matches
        hosts_detail = hosts.get_device_details(ids=hosts_found)["body"]["resources"]
        for detail in hosts_detail:
            # Display the AID and hostname for this match
            aid = detail["device_id"]
            hostname = detail["hostname"]
            print(f"{hostname} ({aid})")
    else:
        print("No hosts found matching that hostname within your Falcon tenant.")
else:
    # Retrieve the details of the error response
    error_detail = hosts_search_result["body"]["errors"]
    for error in error_detail:
        # Display the API error detail
        error_code = error["code"]
        error_message = error["message"]
        print(f"[Error {error_code}] {error_message}")




