
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Select the form and submit with 'rd1' set to 'E'
        return scrapy.FormRequest.from_response(
            response,
            formxpath='//form',  # Adjust the XPath to target your form
            formdata={'rd1': 'E', 'rd2': 'o'},  # Include other fields as necessary
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully')
        # Process the response as needed
