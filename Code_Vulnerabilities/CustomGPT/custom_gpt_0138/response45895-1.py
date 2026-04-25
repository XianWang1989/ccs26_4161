
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Submit the form with the selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/form_submit',  # Change to your form submission URL
            formdata={'rd1': 'E'},  # Selecting the 'Employee' radio button
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully')
