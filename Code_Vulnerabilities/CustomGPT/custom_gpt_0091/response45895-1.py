
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # URL of the page with the form

    def parse(self, response):
        # Define the form data, selecting the appropriate radio button
        formdata = {
            'rd1': 'E',  # Select "Employee"
            'rd2': 'o'   # This value is not needed since it's not selected
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # URL where the form is submitted
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after the form submission
        self.log('Form submitted successfully!')
        # Continue processing the response as needed
