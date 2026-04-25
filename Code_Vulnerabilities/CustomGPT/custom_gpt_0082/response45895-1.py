
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Assuming you're submitting a form
        formdata = {
            'rd1': 'E',  # Selects the Employee radio button
            'rd2': 'o',  # This can be included if necessary
        }

        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Update with the correct form action URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
