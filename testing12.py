import subprocess
import urllib.parse
def searchGoogle(searchString):
    fullGoogle = urllib.parse.quote(searchString)
    subprocess.run("start chrome www.google.com/search?q="+fullGoogle, shell=True)

searchGoogle("search query")
