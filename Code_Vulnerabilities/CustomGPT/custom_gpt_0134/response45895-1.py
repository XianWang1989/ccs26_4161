
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Submit the form with selected radio button
        formdata = {
            'rd1': 'E',  # Selecting the "Employee" radio button
            'rd2': 'o'   # Optional: add this if needed
        }

        yield scrapy.FormRequest(
            url=response.url,  # The URL to submit the form to
            formdata=formdata,
            callback=self.after_form_submission
        )

    def after_form_submission(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
        # Process the response here
