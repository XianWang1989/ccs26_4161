
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Here we submit the form with the appropriate radio button selected
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o',  # You can include this if needed, but it's optional
        }

        yield scrapy.FormRequest(
            url='http://example.com/form-submit',  # URL to submit the form
            formdata=formdata,
            callback=self.parse_result
        )

    def parse_result(self, response):
        # Process the result of the form submission here
        self.log('Form submitted successfully!')
