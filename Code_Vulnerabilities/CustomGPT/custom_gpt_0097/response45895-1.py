
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://example.com/form-page']

    def parse(self, response):
        formdata = {
            'rd1': 'E',  # Selecting the "Employee" option
            'rd2': 'o',  # Not selecting this
        }
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after submission
        self.log('Form submitted successfully!')
