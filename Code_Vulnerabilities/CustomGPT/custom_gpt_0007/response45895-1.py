
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form-url']  # Replace with your target URL

    def parse(self, response):
        # Submit the form with the desired radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the Employee radio button
            'rd2': 'o'   # This can be omitted or can be set if necessary
        }

        yield scrapy.FormRequest(
            url='http://example.com/form-submit-url',  # Replace with the URL where the form is submitted
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Process the response after the form submission
        self.log('Form submitted successfully!')
        # Add your processing logic here

