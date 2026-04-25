
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Selecting the radio button with value 'E'
        formdata = {
            'rd1': 'E',
            'rd2': 'o',  # Include other fields if necessary
        }

        # Submitting the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the actual form's submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
