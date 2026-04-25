
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Submit the form with the correct radio button value
        formdata = {
            'rd1': 'E',  # Select the radio button with value 'E'
            'rd2': 'o',  # This can be included, but it's not needed if not selecting
        }
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form's action URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
