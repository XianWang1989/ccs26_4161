
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Selecting the radio button by sending the form data
        formdata = {'rd1': 'E', 'rd2': 'o'}  # Include other fields if required
        yield scrapy.FormRequest(url=response.url, formdata=formdata, callback=self.after_submission)

    def after_submission(self, response):
        # Handle the response after submitting the form
        self.log('Form submitted successfully!')
