
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Select Employee
            'rd2': '',   # Ensure the other option is not selected
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # URL to submit the form
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log(response.text)
