
import scrapy

class YourSpider(scrapy.Spider):
    name = 'your_spider'

    start_urls = ['http://example.com']

    def parse(self, response):
        # Assuming you want to submit a form
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # This may not be necessary if you only want to select rd1
        }

        # Form submission assuming the form's action URL is known
        yield scrapy.FormRequest(
            url='http://example.com/form-submit-url',  # Replace with actual URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log(f'Response after submission: {response.text}')
