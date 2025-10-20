# xpath 是在XML文档中搜索内容的一门语言
# html 是xml的一个子集
from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周止若</nick>
        <nick class="joy">周大强</nick>
        <nick class="jolin">周星驰</nick>
        <div>
            <nick>惹了1</nick>
        </div>
        <span>
            <nick>惹了2</nick>
        </span>
    </author>

    <partner>
        <nick id="ppc">胖胖东</nick>
        <nick id="ppc">胖胖不陈</nick>
    </partner>
</book>
"""
tree = etree.XML(xml)
# result = tree.xpath("/book/author//nick/text()")
# result = tree.xpath("/book/author/*/nick/text()")
result = tree.xpath("/book//nick/text()")
print(result)