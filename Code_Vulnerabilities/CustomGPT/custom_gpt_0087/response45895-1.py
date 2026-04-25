
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data with the desired radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the "Employee" option
            'rd2': ''    # Not selecting the "Other" option
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit_form',
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after submitting the form
        self.log('Form submitted successfully!')
