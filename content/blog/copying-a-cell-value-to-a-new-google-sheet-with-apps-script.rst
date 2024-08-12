Copying a Cell Value to a New Google Sheet With Apps Script
###########################################################
:date: 2024-08-12 17:00
:author: lofipython
:category: coding, programming, apps script, google sheets
:tags: automating google sheets job, google sheets auto-update, create new row in google sheets apps script
:slug: copying-a-cell-value-to-a-new-google-sheet-with-apps-script
:status: published

I've been messing around with `Apps Script <https://www.google.com/script/start/>`__ lately 
and am finding it useful. The below Apps Script was created with a few prompts to Bing Copilot. First, I asked Bing:

   Write a Google sheets formula that copies the value in cell B10 to another sheet and also fills another column with today's date

...and a later prompt:

   how can i make this script add a new row each time in the target sheet and appending to existing rows?

I refined with some followup prompts to write a script. It copies cell B10's value 
from a sheet then fills in a row in a different sheet with cell B10's value and today's date.

AI allows me to do things that would have taken more time to figure out before. For example,
Bing just tapped the `appendRow <https://developers.google.com/apps-script/reference/spreadsheet/sheet#appendRow(Object)>`__ 
function to handle the updating of values without overwriting existing data. We don't need to know the specific 
Apps Script functions to write code in a new language anymore. AI can just fill in those details for us.

**Apps Script to Copy a Cell Value and Create New Row with Today's Date**

In this case, one sheet is named "Summary" and the other, target sheet is named "Daily".
 
.. code-block:: javascript

   function copyTotalValue() {
     var ss = SpreadsheetApp.getActiveSpreadsheet();
     var sourceSheet = ss.getSheetByName("Summary");
     var targetSheet = ss.getSheetByName("Daily");
     
     // Get the value from B10 in Summary
     var value = sourceSheet.getRange("B10").getValue();
    
     // Get today's date
     var today = new Date();
  
     // Append a new row to the Daily sheet with the value and today's date
     targetSheet.appendRow([value, today]);
   }

According to Bing, Apps Script is a JavaScript dialect:

   Google Apps Script is based on JavaScript. It uses a subset of JavaScript and provides additional built-in functions...


**Automate The Script From the Apps Script Jobs Dashboard**

Go to the Apps Script Jobs dashboard.

.. image:: {static}/images/how-to-find-apps-script-jobs.png
  :alt: Jobs extensions menu to find Apps Script dashboard

Add a new script to run Apps Script.

.. image:: {static}/images/create-new-apps-script-job.png
  :alt: create new apps script code

Click the blue "Add Trigger" button to create a new job.

.. image:: {static}/images/apps-script-jobs.png
  :alt: Apps Script Jobs Triggers Dashboard


**Supplementary Reading**

`Apps Script Reference Overview <https://developers.google.com/apps-script/reference>`__

`Apps Script API <https://developers.google.com/apps-script/api/conceptss>`__

`Apps Script Spreadsheet Service <https://developers.google.com/apps-script/reference/spreadsheet>`__

