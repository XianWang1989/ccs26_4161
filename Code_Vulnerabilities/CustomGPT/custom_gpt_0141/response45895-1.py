
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Prepare form data to select the 'Employee' radio button
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            'rd2': 'o'   # If needed, you can include other radio buttons as well
        }

        # Submit the form
        yield scrapy.FormRequest(
            url=response.url,  # URL of the form submission
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Process the response as needed
