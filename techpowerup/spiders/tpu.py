import scrapy
from scrapy import signals

#Create the urls for both GPUs and CPUs
#The urls are created in a way that only allows less than 101 results to be displayed
#because only 101 search results can be displayed, so the cpu cores and gpu resolutions act as filters to reduce the displayed results
years = range(1998,2024)
resolutions = [0,1,480,720,1080,768,900,1440,2160]
Cores = [1,2,3,4,5,6,8,10,12,14,16,18,20,22,24,26,28,32,36,38,40,48,56,57,60,61,64,68,72,84,9] 
gpu_urls = [f'https://www.techpowerup.com/gpu-specs/?released={year}&performance={resolution}&sort=name' for year in years for resolution in resolutions]
cpu_urls = [f'https://www.techpowerup.com/cpu-specs/?released={year}&nCores={Core}&sort=name' for year in years for Core in Cores]    

class TpuSpider(scrapy.Spider):
    name = 'tpu'
    allowed_domains = ['www.techpowerup.com']
    handle_httpstatus_list = [404,429] 
    start_urls = gpu_urls + cpu_urls #Append both urls lists
    
    #Append all failed urls in a list to retry them separately later
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.failed_urls = []

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(TpuSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.handle_spider_closed, signals.spider_closed)
        return spider

    def parse(self, response):    
        HW = dict()     
        if response.status in [404,429]: # response fails, append to a list to retry it again later 
            self.crawler.stats.inc_value('failed_url_count')
            self.failed_urls.append(response.url)
        else:
            table = response.css('div[id="list"] > table')
            if table: #Check if a table exists
                total = []
                if "gpu" in response.url:
                    columns =['Product_Name','GPU_Chip', 'Released','Bus', 'Memory', 'GPU_clock', 'Memory_clock','Shaders_TMUs_ROPs']
                    HW['Type'] = 'GPU'
                elif "cpu" in response.url:
                    columns = ['Name', 'Codename', 'Cores', 'Clock', 'Socket', 'Process', 'L3 Cache', 'TDP', 'Released'] 
                    HW['Type'] = 'CPU'
                    
                rows = response.css('div[id="list"] > table > tr')
                for row in rows:
                    values = []
                    for td in row.css('td'):
                        info = td.css('a::text').get() or  td.css('::text').get()
                        values.append(info)
                    HW = dict(zip(columns, values))
                    total.append(HW)
                for HW_dict in total:
                    yield HW_dict, response
    
    def handle_spider_closed(self, reason):
        self.crawler.stats.set_value('failed_urls', ', '.join(self.failed_urls))

    def process_exception(self, response, exception, spider):
        ex_class = "%s.%s" % (exception.__class__.__module__, exception.__class__.__name__)
        self.crawler.stats.inc_value('downloader/exception_count', spider=spider)
        self.crawler.stats.inc_value('downloader/exception_type_count/%s' % ex_class, spider=spider)
        
   
                
        
    
    
