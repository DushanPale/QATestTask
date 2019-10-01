import requests

def delete_use_case(use_case_id):
	resp = requests.delete("https://qa-sandbox.apps.htec.rs/use-cases/{}".format(use_case_id))
	print(resp)
	
	# Does not work, but sends back confirmation message (200 OK)
	
if __name__ == "__main__":
	delete_use_case(2034)

