
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form-page']

    def parse(self, response):
        # Form data with radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the "Employee" radio button
            'rd2': 'o'   # You can include other radio buttons if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',
            formdata=formdata,
            callback=self.parse_result
        )

    def parse_result(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Process the response as needed
