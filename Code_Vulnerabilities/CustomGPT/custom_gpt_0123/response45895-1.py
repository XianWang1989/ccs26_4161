
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Create the formdata dictionary with the selected radio button
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            'rd2': 'o'   # You may include this if needed, but it's not checked
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit_form',
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after submitting the form
        self.log('Form submitted successfully!')
