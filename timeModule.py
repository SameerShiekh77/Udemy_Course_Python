import time as t
import html
print(t.time())
print(t.localtime())
time_now = t.localtime()
# t.sleep(10)
print("Transaction Completed " + str(time_now.tm_hour) + "h " + str(time_now.tm_min) + "m")
print(html.unescape("In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;."))