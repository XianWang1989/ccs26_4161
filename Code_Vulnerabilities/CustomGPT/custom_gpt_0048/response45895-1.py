
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Select the value for the radio button
        formdata = {
            'rd1': 'E',  # This selects the 'Employee' radio button
            'rd2': 'o'   # This can be omitted since you're not selecting 'Other'
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form's action URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response from the submission
        self.log('Form submitted successfully')
