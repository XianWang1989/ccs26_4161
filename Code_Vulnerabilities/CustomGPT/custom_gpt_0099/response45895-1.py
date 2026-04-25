
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the formdata
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # Optionally include other radio buttons if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url=response.url,
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after submitting the form
        self.logger.info("Form submitted successfully!")
