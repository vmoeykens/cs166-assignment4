# SQL Injection Fixes
Vincent Moeykens

#### SQL Injection Concept
SQL injection is a method in which one can take advantage of unsterilized user input into SQL queries and escape 
the quote characters in order add their own SQL commands. 

#### What the vulnerability was in the code
In the `sql_injection.py` file, the way user input was inserted into the query string was simply by taking whatever
the user put in the box, and inserting it into string without doing any modification. Since the user input portion
of the query was wrapped in `"` characters, this meant that one could add a "closing" `"` character into their query,
add whatever other SQL commands they desired, then add a trailing `"` character to make it so the query was valid. 

#### How it was fixed
There are a few ways to fix this vulnerability. The best way would be to avoid using raw string construction to create
the queries in the first place, but since that isn't an option for this assignment we have a few other choices. Since
we know that the type of quote character being used in the query construction is a double quote `"`, we can simply
take any instances of the double quote character that the user inputted, and replace it with a single quote character 
`'`. This makes it so the user can never force the query to escape and add their own command. This is done in the line:
```
sanitized_search_term = search_term.replace('"', "'")
```