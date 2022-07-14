import scrapy

class Task(scrapy.Spider):
    name = 'LocalSpider'
    start_urls = ['https://www.aspentimes.com/local']

    def parse(self, response):
        i = 1
        allHeadlines = response.xpath('//*[@id="layout-default"]/h1')

        for i in range(len(allHeadlines)+1):
            name = response.xpath(f'//*[@id="layout-default"]/h1[{i}]//text()').extract()
            content = response.xpath(f'//*[@id="layout-default"]/div[{i}]/article//text()').extract()
            content = [i.replace('\t', '').replace('\n', '') for i in content]
            author = response.xpath(f'//*[@id="layout-default"]/div[{i}]/article/p/a//text()')
            yield{
                'Name' : name,
                'Content' : content,
                'Author' : author
            }
