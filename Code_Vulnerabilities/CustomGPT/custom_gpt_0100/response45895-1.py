
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Select the Employee option
            'rd2': 'o'   # If needed, you can include the other radio button too
        }

        # Submit the form data
        yield scrapy.FormRequest(
            url='http://example.com/form_submission',
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
        # Process the response as needed
