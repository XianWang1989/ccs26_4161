
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Selects the 'Employee' radio button
            'rd2': 'o'   # This can be included, but since 'rd1' is chosen, it won't affect it.
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit', # URL to submit the form
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
