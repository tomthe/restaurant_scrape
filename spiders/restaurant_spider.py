import scrapy


class QuotesSpider(scrapy.Spider):
    name = "restaurant"

    def start_requests(self):
        urls = [
            #'https://www.tripadvisor.com/Restaurants-g187361-Rostock_Mecklenburg_West_Pomerania.html',
            #"https://www.tripadvisor.com/Restaurants-g187361-Rostock_Mecklenburg_West_Pomerania.html"
            "https://www.tripadvisor.com/Restaurants-g187337-Frankfurt_Hesse.html"
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
            "restaurant_url":response.url,
            "rating":response.css("span.ZDEqb::text").get(),
            "reviews1_partial":response.css(".partial_entry").getall(),
            "reviews1_title":response.css(".noQuotes").getall(),
            "reviews1_date_of_visit":response.css("div.prw_rup.prw_reviews_stay_date_hsx").getall(),
            "rank":response.css("span.DsyBj.cNFrA a.AYHFM span b span").getall(),
            "restaurant_category":response.css("html body#BODY_BLOCK_JQUERY_REFLOW.rebrand_2017.js_logging.desktop_web.Restaurant_Review div.page div#atf_header_wrap div#atf_header.ui_container.is-fluid.page-section.accessible_red_3 div#taplc_top_info_0.ppr_rup.ppr_priv_top_info div#component_48.react-container div.lBkqB._T div.vQlTa.H3 span.DsyBj.DxyfE").getall(),
            "restaurant_address1":response.css("html body#BODY_BLOCK_JQUERY_REFLOW.rebrand_2017.js_logging.desktop_web.Restaurant_Review div.page div#MAIN.delineation.accessible_red_3 div#btf_wrap.ui_container.is-fluid.page-section div#taplc_detail_overview_cards_0.ppr_rup.ppr_priv_detail_overview_cards div#component_49.react-container div.hILIJ.MD div.ui_columns div.xLvvm.ui_column.is-12-mobile.is-4-desktop div.YDAvY.R2.F1.e.k div.f.e div.kDZhm.IdiaP.Me span a.YnKZo.Ci.Wc._S.C.FPPgD span.yEWoV").getall(),
            "restaurant_address2":response.css("html body#BODY_BLOCK_JQUERY_REFLOW.rebrand_2017.js_logging.desktop_web.Restaurant_Review div.page div#atf_header_wrap div#atf_header.ui_container.is-fluid.page-section.accessible_red_3 div#taplc_top_info_0.ppr_rup.ppr_priv_top_info div#component_48.react-container div.lBkqB._T div.vQlTa.H3 span.DsyBj.cNFrA span a.AYHFM").getall(),
            "restaurant_open":response.css("div.NehmB").getall(),
            "reviews1_member_info":response.css("div.member_info").getall(),
            "reviewer_user_loc":response.css("div.info_text.pointer_cursor div.userLoc strong").getall(),
            "reviewer_user_name":response.css("div.info_text.pointer_cursor div").getall(),
        }

    def parse_more_reviews(self, response):
        pass
    
        
        #https://www.tripadvisor.com/Restaurant_Review-g187361-d1013055-Reviews-or15-Borwin_Hafenrestaurant-Rostock_Mecklenburg_West_Pomerania.html
        #https://www.tripadvisor.com/Restaurant_Review-g187361-d1013055-Reviews-or30-Borwin_Hafenrestaurant-Rostock_Mecklenburg_West_Pomerania.html