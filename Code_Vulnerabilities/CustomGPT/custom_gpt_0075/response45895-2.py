
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = "radio_buttons_spider"

    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Select Employee radio button
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'rd1': 'E'},
            callback=self.after_post,
            dont_filter=True  # Prevent filtering of this request
        )

    def after_post(self, response):
        if response.status == 200:
            self.log("Form submitted successfully!")
        else:
            self.log(f"Failed to submit form: {response.status}")
