
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your URL

    def parse(self, response):
        # Submit the form selecting the 'Employee' radio button
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o'   # You can include other form fields if needed
        }

        yield scrapy.FormRequest(
            url='http://example.com/form_submit',  # Replace with the form action URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
