
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Prepare the form data with the radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the Employee radio button
            'rd2': 'o'   # This is optional, depending on your needs
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with your form submission URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
