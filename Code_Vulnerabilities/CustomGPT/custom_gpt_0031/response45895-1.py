
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Prepare the form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Select the 'Employee' radio button
            'rd2': 'o'   # You can include this if needed, but it's optional since it's not selected
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form submission URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully')
        # You can now parse the response further
