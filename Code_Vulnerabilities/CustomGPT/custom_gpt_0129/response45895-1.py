
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form-page']  # Replace with your actual URL

    def parse(self, response):
        # Prepare form data with the radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # This can be included if needed; otherwise, omit it
        }

        # Perform form submission
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',  # This should be the action URL of your form
            formdata=formdata,
            callback=self.after_submission  # Callback to handle response after form submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Process the response, e.g., extract data or follow links
