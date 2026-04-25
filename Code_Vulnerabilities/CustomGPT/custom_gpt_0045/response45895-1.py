
import scrapy
from scrapy.http import FormRequest

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Assuming you are submitting a form that has radio buttons
        formdata = {
            'rd1': 'E',  # Select the Employee option
            'rd2': 'o',  # You can include this if necessary, leave it out if you only want rd1
        }

        yield FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Process the response after form submission
        self.log("Form submitted successfully.")
