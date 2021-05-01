from scrapy.cmdline import execute
from os import chdir

chdir("./tutorial")
execute(["scrapy", "crawl", "quotes"])