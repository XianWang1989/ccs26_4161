
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Extract the form action URL
        form_action = response.css('form::attr(action)').get()

        # Prepare the form data, selecting 'E' for radio button 'rd1'
        formdata = {
            'rd1': 'E',   # Select Employee
            'rd2': 'o'    # Include other fields as needed
        }

        # Make the POST request with the form data
        yield scrapy.FormRequest(
            url=response.urljoin(form_action),
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Successfully submitted form!')
        # Continue processing the response as needed
