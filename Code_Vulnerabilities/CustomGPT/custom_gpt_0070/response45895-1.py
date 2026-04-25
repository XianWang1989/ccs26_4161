
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your URL

    def parse(self, response):
        # Prepare form data
        formdata = {
            'rd1': 'E',  # Selecting 'Employee'
            'rd2': 'o'   # This will be ignored since rd1 is selected
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the submission URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Process the response from the submitted form
        self.log('Form submitted successfully!')
        # Additional processing here...
