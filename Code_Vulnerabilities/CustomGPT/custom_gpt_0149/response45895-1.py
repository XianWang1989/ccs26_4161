
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Selecting the radio button 'E' for 'Employee'
        formdata = {
            'rd1': 'E',  # Selecting 'E'
            'rd2': 'o'   # This can be included if needed
        }

        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Change this to your submit URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')

