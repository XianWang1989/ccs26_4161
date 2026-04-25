
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data
        formdata = {'rd1': 'E'}  # This selects the 'Employee' radio button

        # Submit the form
        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Process the response after form submission
        self.log('Form submitted! Response: %s' % response.text)
