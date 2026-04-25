
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Assuming you're submitting a form
        formdata = {
            'rd1': 'E',  # Select the 'Employee' radio button
            'rd2': 'o'   # You can include other fields if necessary
        }
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form's action URL
            method='POST',
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully')
        # Process the response as needed
