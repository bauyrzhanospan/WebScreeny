from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.set_window_size(1024, 1500)

def doit(url):
    url2 = "http://" + str(url[:-1])
    driver.get(url2)
    name = str(url[0:6])+".png"
    driver.save_screenshot(name)

fname = "./1.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

for url in content:
    #doit(url[:-1])
    doit(url)
    print("Did " + str(url))
