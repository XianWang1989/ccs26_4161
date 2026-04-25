
import scrapy

class MySpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']  # Replace with the actual URL

    def parse(self, response):
        # Prepare formdata with selected radio button
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            'rd2': 'o',  # Optionally include other radio buttons
        }

        # Send a POST request with the form data
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form submission URL
            formdata=formdata,
            callback=self.parse_result
        )

    def parse_result(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
        # Continue your processing here
