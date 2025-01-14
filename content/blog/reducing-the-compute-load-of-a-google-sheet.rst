Strategies for Speeding Up a Google Sheet
#########################################
:date: 2025-01-14 11:40
:author: lofipython
:category: Google Sheets, data optimization, 
:tags: optimizing Google Sheet, Google Sheets efficiency, make Google Sheet faster
:slug: reducing-the-compute-load-of-a-google-sheet
:status: published

Recently I had a Google Sheet bogged down so much, Google prompted me to fix it from consuming too many resources in my browser. 
So, I pondered how to speed up my Google Sheet and made a short list of ideas. I included some ideas from a great article from 
Google about `Optimizing Google Sheets <https://support.google.com/docs/answer/12159115?hl=en>`__.

**Strategies for Reducing Load Time in a Google Sheet**

#. Delete all extra columns and rows. Empty rows and columns make the file larger and need to be loaded everytime a Google sheet is accessed. Highlighting and pressing ctrl+D to delete them means they won't be loaded.

#. Change calculation settings to refresh on a change or "every hour" instead of "every minute". This setting affects functions like NOW(), TODAY() and RAND() are recalculated. Select File > Settings and click the "Calculation" tab to adjust your settings.

#. Remove expensive, unnecessary, or old unused functions. Each function you use adds additional load to the Google Sheet. By removing extra functions and charts, it will speed up your Sheet and consume less compute resources. This is unique to each Sheet. Think to yourself, is this part of the document necessary? Is it giving value, or can it be cut?

#. Reduce the number of tabs. Consolidating or removing extra tabs is another way to speed up your load time.

#. Reference data on the same Sheet when possible.

      Reference your data on the same spreadsheet you work on. This is faster than Import functions, such as: IMPORTRANGE, IMPORTDATA, IMPORTXML, IMPORTHTML

      Source: Google, `Optimize your data references to improve Sheets performance <https://support.google.com/docs/answer/12159115?hl=en>`_

#. Use closed range instead of open range references.

      An open range spreadsheet means the range starts and ends without indicating a specific row or column. Example: A:B means the range that includes all cells in columns A and B.

      A closed range reference refers to the range that starts and ends with a specific row or column.   
      Example: A1:B6, A1:C100.
      Open range: A:B
      Closed range: A1:B6

      Source: Google, `Optimize your data references to improve Sheets performance <https://support.google.com/docs/answer/12159115?hl=en>`_

**Conclusion**


Google Sheets are typically very fast until you reach a certain threshold of density. After you reach that point, these changes can speed it up quite a bit!
