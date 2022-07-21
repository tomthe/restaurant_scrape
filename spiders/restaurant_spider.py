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
            link = restau.css("a.Lwqic::attr(href)").get()
            yield response.follow(link, callback=self.parse_one_restaurant)
        
        for a in response.css('.taLnk'):
            yield response.follow(a, callback=self.parse)

    def parse_one_restaurant(self, response):
        yield {
            "restaurant_name":response.css("h1.HjBfq::text").getall(),
            "n_reviews":response.css("span.AfQtZ::text").get(),
             #"restaurant_url":response.css("a.Lwqic::attr(href)").get(),
            "rating":response.css("span.ZDEqb::text").get(),
            "reviews1_partial":response.css(".partial_entry").getall(),
            "reviews1_title":response.css(".noQuotes").getall(),
        }