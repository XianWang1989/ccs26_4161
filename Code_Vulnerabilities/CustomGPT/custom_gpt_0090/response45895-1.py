
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Example data to select radio button "E"
        formdata = {
            'rd1': 'E',  # Selecting the radio button for "Employee"
            'rd2': 'o'   # You may need to include other fields if required
        }

        yield scrapy.FormRequest(
            url='http://example.com/submit',  # URL to submit the form
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after submission
        self.log('Form submitted successfully!')
