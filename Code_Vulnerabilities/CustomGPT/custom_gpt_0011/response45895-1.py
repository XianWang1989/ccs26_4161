
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['YOUR_TARGET_URL']

    def parse(self, response):
        # Specify the form data you want to submit
        formdata = {
            'rd1': 'E',  # Selects the radio button with value 'E'
            # Add other fields if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='YOUR_FORM_SUBMISSION_URL',  # Change it to the form submission URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after the form submission
        self.log('Form submitted successfully.')
        # Add your logic here to process the response
