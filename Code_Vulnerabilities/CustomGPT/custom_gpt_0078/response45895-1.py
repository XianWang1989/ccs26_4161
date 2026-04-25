
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/your-form-page']

    def parse(self, response):
        # Prepare form data
        formdata = {
            'rd1': 'E',  # Select the "Employee" radio button
            'rd2': 'o'   # You can include other fields as needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',  # Change to your submission URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted, now processing the response')
        # Further processing...
