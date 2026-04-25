
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Extract the form action URL
        form_action = response.xpath('//form/@action').get()

        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            'rd2': 'o'   # Optionally fill other radio if needed
        }

        # Submit the form
        yield scrapy.FormRequest(url=form_action, formdata=formdata, callback=self.after_post)

    def after_post(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully!')
