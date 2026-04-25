
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com']  # Replace with your target URL

    def parse(self, response):
        # Prepare the form data, selecting the radio button 'E' for rd1
        formdata = {
            'rd1': 'E',  # Selecting the Employee radio button
            'rd2': 'o'   # Optional: include other radio if needed
        }

        # Make a POST request with the form data
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with your form submission URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully')
        # Further parsing logic here
