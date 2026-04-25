
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Assuming there's a form you need to fill
        formdata = {
            'rd1': 'E',  # Selecting 'Employee'
            'rd2': 'o'   # Selecting 'Other' if needed, but typically only one should be selected
        }

        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Process the response as needed
