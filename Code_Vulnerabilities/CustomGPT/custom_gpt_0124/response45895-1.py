
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Select the radio button by setting its value
        formdata = {
            'rd1': 'E',  # Selecting 'Employee'
            'rd2': 'o'   # Or 'Other' if needed
        }

        # Submit the form with the selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with actual form submission URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully!')
        # Continue with the scraping process
