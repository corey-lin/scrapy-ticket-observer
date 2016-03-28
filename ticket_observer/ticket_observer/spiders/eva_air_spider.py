from scrapy.spider import Spider
from scrapy.http import FormRequest

class EvaAirSpider(Spider):
    name = "eva"
    start_urls = [
        "https://www.evaair.com/en-us/index.html"
    ]

    def parse(self, response):
        formdata = {
            "rbn_Segment" : "1",
            "hid_From" : "SFO",
            "hid_To" : "TPE",
            "hid_lit_date1" : "2016/05/20",
            "hid_lit_date2" : "2016/05/20",
            "ddl_cabinclass" : "EY",
            "rbn_DisplayType" : "1",
            "MainContent_ddl_Adult" : "1",
            "MainContent_ddl_Child" : "0",
            "MainContent_ddl_Infant" : "0"
        }
        yield FormRequest.from_response(response, formdata = formdata, callback = self.parse1)

    def parse1(self, response):
        yield FormRequest.from_response(response, callback = self.parse2)

    def parse2(self, response):
        print response.body
