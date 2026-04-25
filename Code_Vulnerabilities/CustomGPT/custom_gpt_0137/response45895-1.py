
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_buttons'
    start_urls = ['http://example.com/form-page']  # Replace with the actual URL

    def parse(self, response):
        # Preparing form data with radio button selected
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            'rd2': '',   # Not selecting 'Other', you can omit this key if not needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',  # Replace with the URL to submit the form
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle response after form submission
        self.log('Form submitted successfully!')
        # Process the response as needed
