
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare form data
        formdata = {
            'rd1': 'E',  # Select the 'Employee' radio button
            'rd2': 'o'   # Optional, in case you want to select 'Other' too
        }

        # Submit the form with the radio button selection
        yield scrapy.FormRequest(
            url='http://example.com/form-submit',  # Replace with your form submit URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted!')

