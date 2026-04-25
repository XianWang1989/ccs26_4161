
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Select the radio button 'E' (Employee)
        formdata = {
            'rd1': 'E',  # Select Employee
            'rd2': '',   # Other can be omitted if not needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/form_submit',
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully")
