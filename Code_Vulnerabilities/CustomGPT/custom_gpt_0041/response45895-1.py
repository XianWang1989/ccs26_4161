
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Submit the form using the radio button value
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o'   # Optional: Include this if you want to submit other values
        }

        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully')
        # Further processing logic here
