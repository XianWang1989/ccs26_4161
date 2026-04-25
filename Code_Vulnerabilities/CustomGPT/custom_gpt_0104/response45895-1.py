
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Assuming you are submitting a form located at the response URL
        formdata = {
            'rd1': 'E',
            'rd2': '',  # Ensure this is empty if you do not want to select it
        }
        yield scrapy.FormRequest.from_response(
            response,
            formxpath="//form",  # Adjust according to the form's XPath
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle response after the form submission
        self.log("Form submitted successfully!")
        # Add further processing here
