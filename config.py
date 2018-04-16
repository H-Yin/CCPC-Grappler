
# content_url : the URL of All period
# period_re : every period's URL RE
# article_re: every articel's URL RE

#settings.py
ALL_JOURNALS={
    "Journal of Software":{
        "content_url" : u'http://www.jos.org.cn/jos/ch/reader/issue_browser.aspx', 
        "period_re" : u'<a href="issue_list.aspx.*">第.*期</a>', 
        "article_re" : u'<a href="view_abstract.aspx.*"', 
        "author_re" : '', 
        "volumn_re" : '', 
        "column_re" : '', 
        "title_zh_re" : u'<span id="FileTitle">.*</span>', 
        "title_en_re" : u'<span id="EnTitle">.*</span>', 
        "doi_re" : u'<span id="DOI">.*</span>', 
        "abstrace_zh_re" : u'<span id="Abstract">.*</span>', 
        "abstrace_en_re" : u'<span id="EnAbstract">.*</span>', 
        "keywords_zh_re" : u'<span id="KeyWord">.*</span>', 
        "keywords_en_re" : u'<span id="EnKeyWord">.*</span>', 
        "pdf_re" : u'<a href="/jos/ch/reader/create_pdf.aspx.*"', 
        "ref_re" : u'<span id="ReferenceText">.*</span>',
        "to_abstract": False,
    },
    "Computer Enginnering":{
        "content_url" : "http://www.ecice06.com/CN/article/showOldVolumnList.do",
        "period_re" : "<a class=\"J_WenZhang\".*</a>",
        "pdf_re" : u'<a class="J_VM" .*<u>PDF</u></a>',
        "to_abstract" : True,
    },
    "Computer Engineering and Application":{
        
    }
}