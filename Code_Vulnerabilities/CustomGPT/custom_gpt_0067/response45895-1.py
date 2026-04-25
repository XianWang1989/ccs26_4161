
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Assuming you want to submit a form
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o'   # This can be included if needed, but not required for radio
        }

        # Submitting the form
        yield scrapy.FormRequest(
            url='http://example.com/submit_form',  # Replace with your form submission URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted, received response')
