# import library
import scrapy
# Create spider class
class coolSpider(scrapy.Spider):
    # name of the spider
    name = "cool_spider"
    # website url you want to parse
    start_urls = ['https://brickset.com/sets/year-2001']
    # parse the website
    def parse(self, response):
        # CSS selector for images
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            # output link to image, file path, extract file
            yield {
            'Image Link': x.xpath(newsel).extract_first(),
            }

        # To recurse the next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )