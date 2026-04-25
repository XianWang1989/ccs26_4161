
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Fill out the form and select the radio button you want
        formdata = {
            'rd1': 'E',  # Select the radio button with value 'E'
            'rd2': 'o'   # You can also include this if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # URL to submit the form
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully')
        # You can extract data or perform other actions here
