# charusat-result-scrapping

Scrapes semester results [from this URL](http://117.239.83.200:2020/). 
Currently scraper is configured for DEPSTAR CSE 5th Semester results.

## TO-DO
- Automate for other departments.
  - Using Selenium ```Select.options``` object. [Reference](https://stackoverflow.com/questions/35559573/selenium-iterate-through-options-in-dropdown-select)
  - Ideas on finding upperbounds of Class Roll No.
  - Automating Roll numbers. by format  < year >< Institue >< Valid Roll No.>
- Refactor Dataframe of results. The issue is in 'Course Result' Column, the list of dictionary get appended, looks messy :/
- Multithread it possibly?
 
