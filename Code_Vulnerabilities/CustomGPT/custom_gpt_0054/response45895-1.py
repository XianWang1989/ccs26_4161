
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/myform']  # Replace with your form URL

    def parse(self, response):
        # Create the formdata dictionary
        formdata = {
            'rd1': 'E',  # Selecting Employee
            'rd2': ''    # You can leave other radio buttons blank
        }

        # Submit the form with the radio button selection
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with your form submission URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after submission
        self.log('Form submitted successfully.')
