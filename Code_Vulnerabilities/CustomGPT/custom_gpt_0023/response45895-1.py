
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Fill in the form data for radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # Can also set other radio buttons if needed, but this is not necessary for 'E'
        }

        # Perform the POST request with the form data
        yield scrapy.FormRequest(
            url='http://example.com/submit_form',
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
