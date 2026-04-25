
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com']

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # selecting the "Employee" radio button
            'rd2': 'o',  # you can include other fields if necessary
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # replace with the actual form action URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Process the response after form submission
        self.log("Form submitted successfully.")
