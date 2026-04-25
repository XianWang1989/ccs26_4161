
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o',  # You can also include other fields if necessary
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/form_submit',  # Update to your form submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Process the response after submission
        self.log('Form submitted successfully.')
