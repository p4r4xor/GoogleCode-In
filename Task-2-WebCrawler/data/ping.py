import requests

def ping(site_handled):
    #See if the website is up
    global website_url
    try:
        website_url = requests.get(site_handled)
        code = str(website_url.status_code)
    
        if code != "200":
            print("Site unavailable.\nExiting...")
            quit()
        else:
            return website_url
    except requests.exceptions.RequestException:
        print("Website doesn't exist\nQuitting...")
        quit()
