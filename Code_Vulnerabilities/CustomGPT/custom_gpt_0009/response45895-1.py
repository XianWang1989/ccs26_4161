
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = "radio_button_spider"
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Assuming you're navigating to the form page
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//form',  # XPath to locate your form
            formdata={
                'rd1': 'E',  # Selecting the radio button with value 'E'
                # Include other form data as necessary
                # 'rd2': 'o' can also be included if needed
            },
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission here
        self.log('Form submitted successfully!')
