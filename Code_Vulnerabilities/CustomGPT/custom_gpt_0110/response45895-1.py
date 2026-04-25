
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Selecting the radio button with value 'E'
        formdata = {
            'rd1': 'E',  # This selects the 'Employee' radio button
            'rd2': '',   # Leave this empty for 'Other'
        }

        # Submit the form with the radio button selection
        yield scrapy.FormRequest.from_response(
            response,
            formid='my_form_id',  # Replace with the actual form ID or name
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
