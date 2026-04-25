
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        formdata = {
            'rd1': 'E',  # Select the radio button with value 'E'
            'rd2': 'o'   # Optionally include other fields
        }
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form submission URL
            formdata=formdata,
            callback=self.after_post  # The next callback method after form submission
        )

    def after_post(self, response):
        # Handle the response from the form submission
        self.log("Form submitted successfully!")
        # You can process the response here
