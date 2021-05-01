from scrapy.cmdline import execute
from os import chdir, getcwd

chdir("./tutorial")
execute(["scrapy", "crawl", "quotes"])