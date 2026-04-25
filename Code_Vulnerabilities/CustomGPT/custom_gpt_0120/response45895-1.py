
import scrapy

class YourSpider(scrapy.Spider):
    name = 'your_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Form data with radio button selection
        formdata = {
            'rd1': 'E',  # Select "Employee"
            'rd2': 'o'   # This is optional, only if you want to set it too
        }

        # Submit the form with the selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/submit',
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle response after form submission
        self.log('Form submitted successfully!')
        # Process response data here
