
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']  # Replace with the URL of your form

    def parse(self, response):
        # Assuming you are on the form page and need to submit the form here
        formdata = {
            'rd1': 'E',  # Select the radio button for Employee
            'rd2': 'o'   # This value will be ignored since you're selecting rd1.
        }

        # Now, submit the form by following the form action URL
        yield scrapy.FormRequest(
            url=response.url,  # or the action URL of the form
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log("Form submitted successfully!")
        # You can parse the response further as needed
