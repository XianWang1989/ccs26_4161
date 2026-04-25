
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Create a formdata dictionary with the selected radio button
        formdata = {
            'rd1': 'E',  # Select the 'Employee' option
            'rd2': 'o'   # You can include other options if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # The URL to submit the form
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Successfully submitted the form!')
