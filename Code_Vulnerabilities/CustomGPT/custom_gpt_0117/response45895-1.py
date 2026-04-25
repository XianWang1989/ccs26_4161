
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # Optionally include other fields
        }

        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully!')
