
import scrapy

class YourSpider(scrapy.Spider):
    name = 'your_spider'
    start_urls = ['http://yourwebsite.com/form']  # Replace with your target URL

    def parse(self, response):
        # Prepare your form data
        formdata = {
            'rd1': 'E',  # Selecting the Employee radio button
            'rd2': 'o'   # 'Other' radio button (not selected in this case)
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://yourwebsite.com/submit-form',  # Replace with the form's action URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully!')
        # Further processing here
