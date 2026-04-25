
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/my-form']

    def parse(self, response):
        # Select the radio button value
        formdata = {
            'rd1': 'E',  # This selects the "Employee" radio button
            'rd2': 'o'   # The value for the other radio button, if needed
        }

        # Submit the form
        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.parse_results
        )

    def parse_results(self, response):
        # Handle the response from the form submission
        self.log(f'Response URL: {response.url}')
        # Further processing can be done here based on the response
