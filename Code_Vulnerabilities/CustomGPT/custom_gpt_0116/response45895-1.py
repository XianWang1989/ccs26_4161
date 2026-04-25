
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example_spider'
    start_urls = ['http://example.com']  # Replace with your specific URL

    def parse(self, response):
        # Prepare the formdata dictionary to select the radio button
        formdata = {
            'rd1': 'E',  # This selects the 'Employee' radio button
            'rd2': 'o'   # You can also set other fields accordingly
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully!')
