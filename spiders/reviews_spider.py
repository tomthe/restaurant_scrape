import scrapy


class QuotesSpider(scrapy.Spider):
    name = "reviews"

    def start_requests(self):
        urls = [
            #'https://www.tripadvisor.com/Restaurants-g187361-Rostock_Mecklenburg_West_Pomerania.html',
            #"https://www.tripadvisor.com/Restaurants-g187361-Rostock_Mecklenburg_West_Pomerania.html"
            #"https://www.tripadvisor.com/Restaurants-g187337-Frankfurt_Hesse.html",
            #"https://www.tripadvisor.com/Restaurants-g198613-Ostseebad_Kuhlungsborn_Mecklenburg_West_Pomerania.html"
            #"https://www.tripadvisor.com/Restaurants-g187399-Dresden_Saxony.html"
            #"https://www.tripadvisor.com/Restaurants-g187323-Berlin.html"
            #"https://www.tripadvisor.com/Restaurants-g187331-Hamburg.html"
            #"https://www.tripadvisor.com/Restaurants-g187309-Munich_Upper_Bavaria_Bavaria.html"
            "https://www.tripadvisor.com/Restaurants-g187371-Cologne_North_Rhine_Westphalia.html"
            #"https://www.tripadvisor.com/Restaurants-g190454-Vienna.html"
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

        # for review in response.css("div.review-container"):
        #     yield {
        #         "reviewer_user_loc":review.css("div.info_text.pointer_cursor div.userLoc").get(),
        #         "reviewer_user_name":review.css("div.info_text.pointer_cursor div::text").get(),
        #         "restaurant_name":response.css("h1.HjBfq::text").get(),
        #         "reviews1_title":review.css(".noQuotes").getall(),
        #         "reviews1_partial":review.css(".partial_entry").get(),
        #         "reviews1_rating_date":review.css("span.ratingDate::text").getall(),
        #     }
        yield {
            
            "restaurant_name":response.css("h1.HjBfq::text").get(),
            "n_reviews":response.css("span.AfQtZ::text").get(),
            "restaurant_url":response.url,
            "restaurant_website":response.css(".YnKZo::attr(href)").getall(),
            "restaurant_website2":response.css("div.YDAvY.R2.F1.e.k div.f.e div.f::attr(href)").get(),
            "restaurant_phone":response.css("div.f div a::attr(href)").getall(),
            "rating":response.css("span.ZDEqb::text").get(),
            "reviews1_partial":response.css(".partial_entry").getall(),
            "reviews1_partial_text":response.css(".partial_entry::text").getall(),
            "reviews1_title":response.css(".noQuotes").getall(),
            "reviews1_title_text":response.css(".noQuotes::text").getall(),
            "reviews1_date_of_visit":response.css("div.prw_rup.prw_reviews_stay_date_hsx::text").getall(),
            "reviews1_date_of_review":response.css("span.ratingDate::text").getall(),
            "rank":response.css("span.DsyBj.cNFrA a.AYHFM span b span::text").getall(),
            "restaurant_category":response.css("div.lBkqB._T div.vQlTa.H3 span.DsyBj.DxyfE::text").getall(),#html body#BODY_BLOCK_JQUERY_REFLOW.rebrand_2017.js_logging.desktop_web.Restaurant_Review div.page div#atf_header_wrap div#atf_header.ui_container.is-fluid.page-section.accessible_red_3 div#taplc_top_info_0.ppr_rup.ppr_priv_top_info div#component_48.react-container div.lBkqB._T div.vQlTa.H3 span.DsyBj.DxyfE
            "restaurant_category2":response.css("div.lBkqB._T div.vQlTa.H3 span.DsyBj.DxyfE::text").getall(),#html body#BODY_BLOCK_JQUERY_REFLOW.rebrand_2017.js_logging.desktop_web.Restaurant_Review div.page div#atf_header_wrap div#atf_header.ui_container.is-fluid.page-section.accessible_red_3 div#taplc_top_info_0.ppr_rup.ppr_priv_top_info div#component_48.react-container div.lBkqB._T div.vQlTa.H3 span.DsyBj.DxyfE
            "restaurant_address1":response.css("div.hILIJ.MD div.ui_columns div.xLvvm.ui_column.is-12-mobile.is-4-desktop div.YDAvY.R2.F1.e.k div.f.e div.kDZhm.IdiaP.Me span a.YnKZo.Ci.Wc._S.C.FPPgD span.yEWoV::text").getall(),
            "restaurant_address2":response.css("div.lBkqB._T div.vQlTa.H3 span.DsyBj.cNFrA::text").getall(),
            "restaurant_open":response.css("div.NehmB::text").getall(),
            "reviews1_member_info":response.css("div.member_info::text").getall(),
            "reviewer_user_loc":response.css("div.info_text.pointer_cursor div.userLoc::text").getall(),
            "reviewer_user_name":response.css("div.info_text.pointer_cursor div::text").getall(),
            
        }

    def parse_more_reviews(self, response):
        pass
    
        
        #https://www.tripadvisor.com/Restaurant_Review-g187361-d1013055-Reviews-or15-Borwin_Hafenrestaurant-Rostock_Mecklenburg_West_Pomerania.html
        #https://www.tripadvisor.com/Restaurant_Review-g187361-d1013055-Reviews-or30-Borwin_Hafenrestaurant-Rostock_Mecklenburg_West_Pomerania.html