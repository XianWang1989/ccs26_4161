
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form_page']

    def parse(self, response):
        # Extracting form action URL
        form_action = response.css('form::attr(action)').get()

        # Creating form data
        formdata = {
            'rd1': 'E',  # Select the 'Employee' radio button
            'rd2': 'o'   # This will be ignored as 'rd1' is selected
        }

        # Submitting the form
        yield scrapy.FormRequest(
            url=form_action,
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle response after form submission here
        self.log('Form submitted successfully!')
