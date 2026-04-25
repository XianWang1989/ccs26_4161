
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Create a dictionary for the form data
        formdata = {
            'rd1': 'E',  # Select the radio button with value 'E'
            'rd2': 'o'   # Optionally, include other fields if necessary
        }

        # Perform the POST request with the selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with form submission URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after the form submission
        self.log("Form successfully submitted!")
        # Additional parsing logic goes here
