
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form-page']

    def parse(self, response):
        # Creating the formdata dictionary
        formdata = {
            'rd1': 'E',  # Select the radio button with value 'E'
            'rd2': 'o'   # Optionally, you can include other fields
        }

        # Sending the POST request
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',  # Update with the correct URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
