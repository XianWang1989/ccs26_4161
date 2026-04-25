
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Assuming you need to follow a link to get to the form
        # If the form is on the start URL, this can be skipped.

        # here you submit the form with the desired radio button checked
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'rd1': 'E', 'rd2': 'o'},  # Selecting 'Employee' radio button
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after the form submission
        self.log("Form submitted successfully!")
