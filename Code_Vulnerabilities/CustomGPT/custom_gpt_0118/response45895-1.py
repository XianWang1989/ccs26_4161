
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Select the 'Employee' radio button
            'rd2': 'o'   # This can be excluded if not needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # URL that processes the form
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
        # Additional processing here
