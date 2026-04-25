
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Submit the form with the selected radio button
        formdata = {
            'rd1': 'E',  # Select the radio button for Employee
            'rd2': 'o'   # This line is not necessary if 'rd1' is checked
        }

        yield scrapy.FormRequest(
            url=response.url,
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
