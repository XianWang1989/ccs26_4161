
import scrapy

class MySpider(scrapy.Spider):
    name = 'radio_button_example'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Create a dictionary for the form data
        formdata = {
            'rd1': 'E',  # Select the Employee radio button
            'rd2': 'o'   # This will remain unchecked
        }

        # Submit the form with the selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',  # URL where the form is submitted
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # You can extract information from the response here
