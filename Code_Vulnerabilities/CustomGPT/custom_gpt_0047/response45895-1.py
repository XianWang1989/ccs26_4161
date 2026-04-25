
import scrapy

class MySpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com']  # Replace with your target URL

    def parse(self, response):
        # Fill in the form data, selecting the radio button
        formdata = {
            'rd1': 'E',  # Select 'Employee'
            'rd2': 'o'   # Select 'Other' if needed, but you typically don't include unselected values
        }

        # Submit the form (replace 'your_form_action_url' with the actual form action URL)
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the actual URL to submit the form
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
