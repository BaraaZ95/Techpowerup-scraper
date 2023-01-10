# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


gpu_columns =['Product_Name','GPU_Chip', 'Released','Bus', 'Memory', 'GPU_clock', 'Memory_clock','Shaders_TMUs_ROPs']
            
cpu_columns = ['Name', 'Codename', 'Cores', 'Clock', 'Socket', 'Process', 'L3 Cache', 'TDP', 'Released']

#The Item pipeline stores two separate csvs, one for the cpus and another for the gpus based on the url of the response
class TechpowerupPipeline:

    def __init__(self):
        self.cpu_file = open("cpus.csv", "w")
        self.gpu_file = open("gpus.csv", "w")
        self.cpu_writer = csv.DictWriter(self.cpu_file, fieldnames=cpu_columns)
        self.gpu_writer = csv.DictWriter(self.gpu_file, fieldnames=gpu_columns)
        self.cpu_writer.writeheader()
        self.gpu_writer.writeheader()

    def process_item(self, item, spider):
        if "cpu" in spider.response.url:
            self.cpu_writer.writerow(item)
        elif "gpu" in spider.response.url:
            self.gpu_writer.writerow(item)

    def close_spider(self, spider):
        self.cpu_file.close()
        self.gpu_file.close()

