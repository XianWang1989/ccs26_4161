
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Create the form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Selecting 'Employee'
            'rd2': 'o'   # Optional if you want to handle the second radio button
        }

        # Send a POST request with the form data
        yield scrapy.FormRequest(
            url='http://example.com/form/submit',
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Process the response as needed
