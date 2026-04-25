
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        formdata = {
            'rd1': 'E',  # Selecting the "Employee" radio button
            'rd2': 'o'   # This can be included if needed
        }
        yield scrapy.FormRequest(
            url='http://example.com/form_submit',  # URL to submit the form
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after submitting the form
        self.log('Form submitted successfully')
