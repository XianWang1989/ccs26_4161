
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with the actual URL

    def parse(self, response):
        # Form data to submit
        formdata = {
            'rd1': 'E',  # Select the 'Employee' radio button
            'rd2': 'o'   # Other radio button, if needed
        }
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the actual URL to submit the form
            method='POST',
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Further processing here
