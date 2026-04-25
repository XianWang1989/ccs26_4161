
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form-page']

    def parse(self, response):
        # Create the form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Select the 'Employee' radio button
            'rd2': 'o'   # This can be omitted or set to a different value if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after submitting the form
        self.log('Form submitted successfully!')
