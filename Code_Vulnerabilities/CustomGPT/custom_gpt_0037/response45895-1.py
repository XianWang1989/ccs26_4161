
import scrapy

class YourSpider(scrapy.Spider):
    name = 'your_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Selecting the radio button 'E' for 'Employee'
        formdata = {
            'rd1': 'E',  # Selecting Employee
            'rd2': 'o'   # You can include this if needed, otherwise omit
        }

        # Sending a POST request with the selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Update with the form submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted, response received.')
