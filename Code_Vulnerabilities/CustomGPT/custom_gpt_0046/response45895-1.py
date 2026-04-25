
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/your-form-page']

    def parse(self, response):
        # Preparing form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Selects the Employee radio button
            'rd2': 'o'   # This can be included, but is not needed for 'E'
        }

        # Assuming the form's action URL is /submit-form
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after submitting the form
        self.log('Form submitted successfully!')
