import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml','r')as file:
    yaml_data=yaml.safe_load(file)
    rss_element=xml_tree.Element('rss',{
         'version':"2.0",
         'xmlns:itunes':"http://www.itunes.com/dtds/podcast-1.0.dtd",
         'xmlns:atom':"http://www.w3.org/2005/Atom",
         'xmlns:content':"http://purl.org/rss/1.0/modules/content/" 
    })


channel_elemnt=xml_tree.SubElement(rss_element,"channel")
xml_tree.SubElement(channel_elemnt,'title').text=yaml_data['title']
output_tree=xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml',encoding='UTF-8',xml_declaration=True)