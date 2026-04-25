
import scrapy


class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Construct the form data
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # Include other radio button values if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/form_submission',  # Replace with the form's action URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully!')
        # Do more with the response here
