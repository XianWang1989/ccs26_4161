
import scrapy

class RadioButtonsSpider(scrapy.Spider):
    name = "radio_buttons"
    start_urls = ['http://example.com']  # Replace with the URL of the form you are targeting

    def parse(self, response):
        # Extract the form action URL (update this depending on the actual form)
        form_action = response.css('form::attr(action)').get()
        if form_action:
            yield scrapy.FormRequest(
                url=response.urljoin(form_action),
                formdata={'rd1': 'E', 'rd2': ''},  # Selecting the radio button 'E'
                callback=self.after_submit
            )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully! Response:')
        self.log(response.body)
