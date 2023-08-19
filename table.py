import scrapy



def fifth(lst):
    start =0
    end =5

    while end <= len(lst):
        yield lst[start: end]
        start +=5
        end +=5

class TableSpider(scrapy.Spider):
    name = "table"
    allowed_domains = ["espn.com"]
    start_urls = ["https://www.espn.com/soccer/standings/_/league/UEFA.CHAMPIONS/season/2021"]

    def parse(self, response):
        dt ={
            
        }

        team_row= response.css("table")[0].css("tr")
        detail_row= response.css("table")[1].css("tr")

        for group, group_detail in zip(
            fifth(team_row), fifth(detail_row)
        ):
            group_label = group[0].css("td span::text").get()

            dt[group_label]={}

            for team, detail in zip(group[1:], group_detail[1:]):
                team_label = team.css("td span.hide-mobile a::text").get()

                table_detail = detail.css("td span::text").getall()
                dt[group_label][team_label]= {
                    "wins": table_detail[1],
                    "draws": table_detail[2],
                    "loses": table_detail[3],
                    "points": table_detail[-1]
                }

        yield dt       

