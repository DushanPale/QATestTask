import requests

def main():
	resp = requests.delete("https://qa-sandbox.apps.htec.rs/use-cases/2034")
	print(resp)
	
	
	
	
if __name__ == "__main__":
	main()

