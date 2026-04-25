
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Define your form data
        formdata = {
            'rd1': 'E',  # Select the value for the first radio button
            'rd2': 'o'   # You can also set other parameters if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # URL where the form is submitted
            formdata=formdata,
            callback=self.parse_results
        )

    def parse_results(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully")
