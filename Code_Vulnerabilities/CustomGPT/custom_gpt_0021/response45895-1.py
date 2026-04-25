
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Fill the form and submit it
        formdata = {
            'rd1': 'E',  # Selects the Employee radio button
            'rd2': 'o'   # You can include other fields as necessary
        }
        yield scrapy.FormRequest(
            url=response.url,  # The same URL or the action URL of the form
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
