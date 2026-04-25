
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Selecting the radio button for Employee
            'rd2': 'o'   # You can include this if needed, but it's not required for selecting rd1
        }

        # Send the POST request with formdata
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # URL where the form is submitted
            method='POST',
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully.')
