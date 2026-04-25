
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'

    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Fill in the formdata with the radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # This can be omitted or set accordingly
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form action URL
            method='POST',
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully.')
