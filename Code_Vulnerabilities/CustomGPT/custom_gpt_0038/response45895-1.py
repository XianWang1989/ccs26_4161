
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # You can also include other options if needed
        }

        # Submit the form with selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the actual form submission URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Extract data or perform further actions here
