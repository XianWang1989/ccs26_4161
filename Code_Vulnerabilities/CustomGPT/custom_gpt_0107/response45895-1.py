
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'

    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Submitting the form with radio button selection
        formdata = {
            'rd1': 'E',  # Selecting 'Employee'
            'rd2': 'o'   # You can include this if needed, but not necessary for rd1
        }

        yield scrapy.FormRequest(
            url='http://example.com/submit',
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted!')
