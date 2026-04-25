
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Extracting the form action URL (if necessary)
        form_action = response.css('form::attr(action)').get()

        # Creating the form data dictionary
        formdata = {'rd1': 'E', 'rd2': 'o'}  # Selecting 'E' for Employee

        # Submitting the form
        yield scrapy.FormRequest(
            url=response.urljoin(form_action),
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission here
        self.log("Form submitted successfully")
