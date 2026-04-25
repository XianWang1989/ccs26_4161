
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data with the selected radio button
        formdata = {
            'rd1': 'E',  # Selecting radio button with value 'E'
            'rd2': 'o'   # You can include other parameters as needed
        }

        # Submit the form with the selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Change to the form's action URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # Add additional parsing logic here
