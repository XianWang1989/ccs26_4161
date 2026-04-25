
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data with the selected radio button
        formdata = {
            'rd1': 'E'  # Selecting the Employee radio button
        }
        # Submit the form with the selected radio button
        yield scrapy.FormRequest(
            url=response.url,
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # You can now parse the response as needed
