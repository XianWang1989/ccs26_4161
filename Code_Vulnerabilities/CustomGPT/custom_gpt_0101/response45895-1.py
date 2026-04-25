
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        formdata = {'rd1': 'E'}  # Selecting the radio button with value 'E'
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission here
        self.log('Form submitted successfully')
