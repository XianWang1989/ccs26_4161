
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with the actual URL

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Selecting the radio button 'E'
            'rd2': 'o',  # Optional: include other fields if necessary
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the actual form submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
