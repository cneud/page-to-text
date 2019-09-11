#!/usr/bin/env python
# Usage: python page_to_text.py <page-xml-file>

import codecs
import os
import sys
import xml.etree.ElementTree as ET


if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    namespace = {'page_2009-03-16': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2009-03-16',
                 'page_2010-01-12': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-01-12',
                 'page_2010-03-19': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19',
                 'page_2013-07-15': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15',
                 'page_2016-07-15': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2016-07-15',
                 'page_2017-07-15': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2017-07-15',
                 'page_2018-07-15': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2018-07-15',
                 'page_2019-07-15': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15'}
    tree = ET.parse(sys.argv[1])
    xmlns = tree.getroot().tag.split('}')[0].strip('{')
    if xmlns in namespace.values():
        for regions in tree.iterfind('.//{%s}TextEquiv' % xmlns):
            sys.stdout.write('\n')
            for region in regions.findall('{%s}Unicode' % xmlns):
                text = region.text
                sys.stdout.write(text)
    else:
        print('ERROR: Not a valid PAGE xml file (namespace declaration missing)')
