
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form_page']

    def parse(self, response):
        # Fill in the form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Select Employee radio button
            'rd2': 'o'   # Other radio button (not selected)
        }

        # Submit the form
        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Process the response from the form submission
        self.log('Form submitted! Response received.')
