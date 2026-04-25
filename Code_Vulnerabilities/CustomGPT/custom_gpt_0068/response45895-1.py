
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with the actual URL of the form

    def parse(self, response):
        # Prepare the form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Selecting the Employee radio button
            'rd2': 'o',  # Can be included if needed, but should remain empty if not selected
        }

        # Submit the form (make sure to change 'form_action' to the actual action URL)
        yield scrapy.formrequest.FormRequest(
            url='http://example.com/form_action',  # Replace with the actual action URL of the form
            formdata=formdata,
            callback=self.parse_result  # Callback to handle the response
        )

    def parse_result(self, response):
        # Handle the response after the form submission
        self.log('Form submitted successfully!')
        # You can extract data, handle errors, etc.
