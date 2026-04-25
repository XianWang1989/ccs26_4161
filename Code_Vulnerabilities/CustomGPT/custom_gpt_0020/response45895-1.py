
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Define the form data you want to submit
        formdata = {
            'rd1': 'E',  # selecting the radio button with value 'E'
            'rd2': 'o'   # you can include this in case you need to submit both
        }

        # Submit the form with selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/form_submit',  # URL to submit the form
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully!')
        # You can extract data or follow links here
