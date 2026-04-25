
import scrapy

class YourSpider(scrapy.Spider):
    name = 'your_spider'
    start_urls = ['http://example.com']  # Replace with your target URL

    def parse(self, response):
        # Assuming you're filling a form with radio button selections
        formdata = {
            'rd1': 'E',  # Select Employee
            'rd2': 'o'   # Optionally select Other if needed
        }

        yield scrapy.FormRequest(
            url='http://example.com/form_submit',  # Replace with the form submission URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted, response obtained!')
