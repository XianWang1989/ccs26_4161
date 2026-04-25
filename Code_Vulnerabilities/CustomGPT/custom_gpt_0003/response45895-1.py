
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with the target URL

    def parse(self, response):
        # Here, we're sending a POST request to the form's action URL
        yield scrapy.FormRequest(
            url='http://example.com/form_action',  # Replace with the action URL of the form
            formdata={'rd1': 'E', 'rd2': 'o'},  # Select 'E' for rd1
            callback=self.after_post  # The callback function after form submission
        )

    def after_post(self, response):
        # Handle the response after submitting the form
        self.log("Form submitted, here is the response:")
        self.log(response.text)
