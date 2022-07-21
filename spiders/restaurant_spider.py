import scrapy


class QuotesSpider(scrapy.Spider):
    name = "restaurant"

    def start_requests(self):
        urls = [
            'https://www.tripadvisor.com/Restaurants-g187361-Rostock_Mecklenburg_West_Pomerania.html',
            #"https://www.tripadvisor.com/Restaurants-g187361-Rostock_Mecklenburg_West_Pomerania.html"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.css('small.author::text').get(),
        #         'tags': quote.css('div.tags a.tag::text').getall(),
        #     }

        for restau in response.css("div.YHnoF"):
            link = restau.css("a.Lwqic").get()
            yield {
                "restaurant_name":restau.css("a.Lwqic::text").getall(),
                "n_reviews":restau.css("span.IiChw::text").get(),
                "restaurant_url":restau.css("a.Lwqic::attr(href)").get(),
                "rating":restau.css("svg::attr(aria-label)").get()
            }
        
        for a in response.css('.taLnk'):
            yield response.follow(a, callback=self.parse)