from datetime import datetime

now = datetime.now()

print(type(now))

print(now.strftime("%d %B %Y"))