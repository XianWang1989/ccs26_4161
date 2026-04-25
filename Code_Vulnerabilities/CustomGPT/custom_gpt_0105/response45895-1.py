
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Assuming you're on the page with the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form's submission URL
            formdata={
                'rd1': 'E',  # Select the Employee radio button
                'rd2': 'o'   # Include other fields if necessary
            },
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully.')
