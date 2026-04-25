
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Prepare form data to submit
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            'rd2': 'o'   # Include this if you want to select 'Other' as well, but it's not needed here
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the actual form submission URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Process response after form submission
        self.log('Form submitted successfully!')
        # Continue with further parsing here
