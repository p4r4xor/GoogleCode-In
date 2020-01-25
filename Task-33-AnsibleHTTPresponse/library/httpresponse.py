import requests
from ansible.module_utils.basic import *
website = "https://codein.withgoogle.com/"
module = AnsibleModule(argument_spec={})
try:
	r = requests.head(website)
	response = r.status_code
except requests.ConnectionError:
	print("Couldn't connect. Try another website or Try again.")
module.exit_json(changed=False, Status_Code=response)

