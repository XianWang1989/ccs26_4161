
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form-page']  # Replace with your target URL

    def parse(self, response):
        # Assuming there's a form action you want to submit
        form_action = response.css('form::attr(action)').get()

        # Set the formdata with the radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            # You can add other form fields if needed
            'rd2': 'o',  # If you want to include 'Other' option as well
        }

        yield scrapy.FormRequest(
            url=response.urljoin(form_action),
            method='POST',
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
