
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # replace with the URL of your form

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            # Include other form fields if necessary
        }

        # Submit the form
        yield scrapy.FormRequest(
            url=response.url,  # URL where the form is submitted
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
