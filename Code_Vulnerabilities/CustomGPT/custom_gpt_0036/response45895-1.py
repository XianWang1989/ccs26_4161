
import scrapy


class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://example.com/form']  # Replace with the actual URL of the page with the form

    def parse(self, response):
        # This is where you would fill out the form with your choices
        formdata = {
            'rd1': 'E',  # Selecting the 'Employee' radio button
            'rd2': 'o'   # If you need to submit for other fields, you may include them as necessary
        }

        # Submit the form with the selected radio button
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the actual form submission URL
            formdata=formdata,
            callback=self.after_submit
        )

    def after_submit(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # You can extract data from the response here as needed
