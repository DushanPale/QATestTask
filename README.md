Task work flow:

There is code for autmatic deletion of cases. It is made so it can delete every case just by changing case ID in code line.
Unfotunately it does not work. Although response that i get is confimrative: (200 OK)


Using POSTMAN I  tried using different requests beside DELETE, but notthing happened.

Than I poked around DevTools and figured got an Idea to find API endpoint, since Delete button on qa-sandbox.apps.htec.rs/use-cases/
is actually working.

I found out that for "test auto" API endpoint is https://qa-sandbox.apps.htec.rs/api/usecases/2040 I also tried deleting ot with Python file
 pyReq.py and with POSTMAN, but Authoriyation was the issue. At this point I didnt have more time or knowledge for the task given, considering
 that I do not have any documentation.
 
 
 P.S. I was not sure if I was ment to write all this as a report on website or here, I hope this is fine.
 
 
