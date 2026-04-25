
import scrapy

class MySpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Define the form data you want to submit
        formdata = {
            'rd1': 'E',  # Select Employee radio button
            'rd2': 'o'   # You can include this if necessary
        }

        # Submit the form with the selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/form-submit',  # Replace with the form submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully')
        # Process the response...
