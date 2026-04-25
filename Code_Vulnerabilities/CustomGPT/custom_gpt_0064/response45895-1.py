
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Define form data with the selected radio button
        formdata = {
            'rd1': 'E',  # This selects the 'Employee' option
            'rd2': 'o'   # This can be included if needed
        }

        # Submit the form with selected radio button
        yield scrapy.FormRequest(
            url=response.url,  # URL where the form is submitted
            formdata=formdata,
            callback=self.after_form_submission
        )

    def after_form_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted! Response received.')
        # Further processing...
