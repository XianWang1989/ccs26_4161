
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with the actual URL

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o'   # You can include this if needed, but it will not be selected
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form's action URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Process the response after form submission
        self.log('Form submitted. Response URL: {}'.format(response.url))
