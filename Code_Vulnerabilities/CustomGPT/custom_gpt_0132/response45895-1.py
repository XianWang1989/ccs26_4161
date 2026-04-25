
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Select radio button 'E' for the 'rd1' input
        formdata = {'rd1': 'E', 'rd2': 'o'}  # Include other fields if needed
        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Process the response after the form submission
        self.log("Form submitted successfully!")
