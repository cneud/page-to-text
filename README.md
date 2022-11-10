# page-to-text
Extracts the text from a [PAGE](http://primaresearch.org/publications/ICPR2010_Pletschacher_PAGE) file and writes it to `stdout`.

Note that this tool does not consider `ReadingOrder` if available in the PAGE-XML, but instead writes output based of the order in the XML tree.

Use like:

    python page_to_text.py <page-xml-file>
