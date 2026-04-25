
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare formdata, selecting 'E' for the 'rd1' radio button
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # You can include this if necessary
        }

        # Make a POST request with the formdata
        yield scrapy.FormRequest(
            url='http://example.com/submit',
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after submission
        self.log('Form submitted successfully!')
