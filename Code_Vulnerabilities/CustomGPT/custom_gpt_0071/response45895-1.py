
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # replace with your target URL

    def parse(self, response):
        # Form data to submit
        formdata = {
            'rd1': 'E',  # selecting the 'Employee' radio button
            'rd2': 'o',  # if needed, include other radio buttons
        }

        # Send the form submission
        yield scrapy.FormRequest(
            url=response.url,  # URL where the form is submitted
            method='POST',
            formdata=formdata,
            callback=self.after_post  # define the next parsing method
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Process the response as needed
