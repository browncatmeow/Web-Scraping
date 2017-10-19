import requests, os, sys, bs4, re

# Create folder if the folder 'imgur' currently does not exist.
path = os.makedirs('./imgur',exist_ok=True)

res = requests.get('http://imgur.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status() 
soup = bs4.BeautifulSoup(res.text, "html.parser")
matches = [img.find('img')['src'] for img in soup.find_all('a',attrs={'class':'image-list-link'})]

dlurl = ['http:'+ url for url in matches]
print(len(dlurl))
for link in dlurl:
    print('Downloading images %s...' %(link))
    res = requests.get(link)
    res.raise_for_status()
    
    
    
    imageFile = os.path.join('./imgur',os.path.basename(link))
    with open(imageFile,'wb') as f:
        for chunk in res:
            f.write(chunk)
