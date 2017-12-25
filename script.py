from selenium import webdriver


# Browser created
driver = webdriver.Chrome("./chromedriver")
driver.set_window_size(1024, 1500)


# Function that takes screenshot
def doit(url):
    url2 = "https://" + str(url) # Change here if no https and only http
    driver.get(url2)
    name = str(url)+".png"
    driver.save_screenshot(name)

fname = "./1.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

for url in content:
    #doit(url[:-1])
    doit(url)
    print("Made screenshot of " + str(url))
print("That is all! Check folder and put star for my developer!")
