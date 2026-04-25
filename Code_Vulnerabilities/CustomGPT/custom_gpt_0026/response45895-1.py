
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Filling out the form with the radio button selection
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            # Include other fields if necessary
        }

        # Submit the form
        yield scrapy.FormRequest(
            url=response.url,
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Process the response further as needed
