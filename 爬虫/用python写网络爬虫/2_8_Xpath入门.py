#Xpath 是在XML文档中搜索内容的一门语言
#html是xml的一个子集
'''
<book>
   <id>1</id>
   <name>野花遍地香</name>
   <price>1.23</price>
   <author>
       <nick>周大强</nick>
       <nick>周芷若</nick>
   </author>
</book>
'''

#安装lxml模块
#pip install lxml -i xxxxxxxx
#Xpath解析
from lxml import etree

xml = '''
<book>
   <id>1</id>
   <name>野花遍地香</name>
   <price>1.23</price>
   <nick>臭豆腐</nick>
   <author>
       <nick id="10086">周大强</nick>
       <nick id="10010">周芷若</nick>
       <nick class="joy">周杰伦</nick>
       <nick class="jolin">蔡依林</nick>
       <div>
          <nick>惹了</nick>
       </div>
   </author>
</book>
'''
tree = etree.XML(xml)
result = tree.xpath("/book/author/nick/text()") #/表示层级关系。第一个/是根节点
print(result)



