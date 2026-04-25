
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Define the form data including selected radio button
        formdata = {
            'rd1': 'E',  # Selecting 'Employee'
            'rd2': 'o',  # Optionally include other radio buttons if needed
        }

        # Submit the form using a POST request
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form action URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully.')
        # Process the response here
