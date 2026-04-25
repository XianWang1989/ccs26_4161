
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Send the form data with the selected radio button
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'rd1': 'E', 'rd2': 'o'},  # Select 'E' for rd1
            callback=self.after_form_submission
        )

    def after_form_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted!')

        # Continue processing the response
