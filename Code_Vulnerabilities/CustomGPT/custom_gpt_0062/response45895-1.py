
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com']  # Replace with your target URL

    def parse(self, response):
        # Prepare form data with selected radio button
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            'rd2': 'o'   # Optional if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the URL to submit the form
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
