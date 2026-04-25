
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form-page']

    def parse(self, response):
        # Submitting the form with the selected radio button
        formdata = {
            'rd1': 'E',  # Selecting the "Employee" radio button
            'rd2': 'o',  # Optionally include the other radio button as 'Other'
        }

        yield scrapy.FormRequest(
            url='http://example.com/submit-form',  # Change to your target form URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
