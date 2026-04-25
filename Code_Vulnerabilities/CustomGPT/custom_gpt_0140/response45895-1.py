
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Define the form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Selecting the "Employee" radio button
            'rd2': 'o',  # Optionally include other fields if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the actual form submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after submitting the form
        self.log('Form submitted! Response: {}'.format(response.text))
