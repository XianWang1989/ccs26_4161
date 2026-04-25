
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with the URL of the form

    def parse(self, response):
        # Create a dictionary with the radio button selection
        formdata = {
            'rd1': 'E',  # Select the radio button with value 'E'
            'rd2': 'o'   # Optional: you can still include other fields if necessary
        }

        # Submit the form
        yield scrapy.FormRequest(
            url=response.url,  # URL to submit the form to
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
        # You can extract data from the response here
        # For example, print the page content or extract specific information
        self.log(response.text)
