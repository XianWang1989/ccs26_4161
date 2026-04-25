
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form-page']

    def parse(self, response):
        # Here you can extract any necessary data before the form submission

        # Construct the formdata with the correct radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # This is optional, you can exclude if not needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit-form',  # Update with the actual form submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after the form submission
        self.log('Form submitted successfully!')
