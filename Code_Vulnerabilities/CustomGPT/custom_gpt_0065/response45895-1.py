
import scrapy

class SampleSpider(scrapy.Spider):
    name = "sample_spider"
    start_urls = ['http://example.com/form']  # Replace with your form URL

    def parse(self, response):
        # Fill out the form and select the radio button
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            'rd2': 'o'   # You can include this if needed, but it's optional for non-selected radio buttons
        }

        # Submit the form
        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully.')
        # Process the response as needed
