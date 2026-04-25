
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'

    start_urls = ['http://example.com/form']  # Replace with the actual URL

    def parse(self, response):
        # Submit the form with selected radio button
        formdata = {
            'rd1': 'E',  # Select Employee
            'rd2': '',   # Ensure 'Other' is not selected
        }

        yield scrapy.FormRequest.from_response(
            response,
            formname='my_form',  # Replace 'my_form' with the actual form name if necessary
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Process the response as needed
