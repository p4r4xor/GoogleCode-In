import requests
from bs4 import BeautifulSoup
links = []

def cr(soup, website_url, site, file):
    try:

        for link in soup.find_all('a', href=True):
            link = link.get('href')
            if link not in links:
                    if link.startswith("http"):
                        website_url = requests.get(link)
                        code = str(website_url.status_code)
                        if code == "200":
                            links.append(link)
                            print(link)
                    elif link.startswith("/"):
                        link = site + link
                        if link not in links:
                            website_url = requests.get(link)
                            code = str(website_url.status_code)
                            if code == "200":
                                links.append(link)
                                print(link)
        for link in soup.find_all('a', href=True):
            link = link.get('href')
            if link not in links:
                    if link.startswith("http"):
                        website_url = requests.get(link)
                        code = str(website_url.status_code)
                        if code == "200":
                            links.append(link)
                            print(link)
                    elif link.startswith("/"):
                        link = site + link
                        if link not in links:
                            website_url = requests.get(link)
                            code = str(website_url.status_code)
                            if code == "200":
                                links.append(link)
                                print(link)
        for i in links:
            website_url = requests.get(i)
            soup = BeautifulSoup(website_url.content,'html.parser',from_encoding="iso-8859-1")
            for link in soup.find_all('a', href=True):
                link = link.get('href')
                if link not in links:
                    if link.startswith(site):
                        website_url = requests.get(link)
                        code = str(website_url.status_code)
                        if code == "200":
                            links.append(link)
                            print(link)

                    elif link.startswith("/"):
                        link = site + link
                        if link not in links:
                            website_url = requests.get(link)
                            code = str(website_url.status_code)
                            if code == "200":
                                links.append(link)
                                print(link)
            if file:
                f = open(file, "w+")
                for i in links:
                    f.write(i)
                    f.write("\n")
                f.close
    except KeyboardInterrupt:
        print("\nCtrl+C Pressed\nQuitting.")
        if file:
            f = open(file, "w+")
            for i in links:
                f.write(i)
                f.write("\n")
            f.close
        quit()
