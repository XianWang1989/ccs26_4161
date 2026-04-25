
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Create a FormRequest to submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the action URL of the form
            formdata={'rd1': 'E', 'rd2': 'o'},  # Select 'E' for rd1
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Process the response as needed
