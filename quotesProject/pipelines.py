# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# # useful for handling different item types with a single interface
from itemadapter import ItemAdapter
class QuotesprojectPipeline:
    def process_item(self, item, spider):
        return item

# from itemadapter import ItemAdapter
# #import sqlite3
# import mysql.connector

# class QuotesprojectPipeline:
#     def __init__(self):
#         self.create_connection()
#         self.create_table()

#     def create_connection(self):
#         #self.conn = sqlite3.connect('sqlite3.db')
#         self.conn = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             password = 'Test@1234',
#             database = 'scrapy',
#         )
#         self.curr = self.conn.cursor()

#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS quotes """)
#         self.curr.execute("""
#                  create table quotes(
#                      title text,
#                      author text,
#                      tab text)
#              """)

#     def process_item(self, item, spider):
#         self.store_db(item)
#         # print('items.....'+ item["iTitle"][0])
#         return item

#     def store_db(self, item):
#         # self.curr.execute("""insert into quotes values(?,?,?)""",(
#             # item["iTitle"][0],
#             # item["iAuth"][0],
#             # item["iTag"][0]
#             # ))
#         self.curr.execute("""insert into quotes values(%s,%s,%s)""",(
#             item["iTitle"][0],
#             item["iAuth"][0],
#             item["iTag"][0]
#             ))
#         self.conn.commit()
