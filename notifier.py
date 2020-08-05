# pip install notify2

import time
import notify2
from content import topStories

# path to notification window icon
ICON_PATH = "icon.jpg"

# fetch news items
newsitems = topStories()

notify2.init("News Notifier")
n = notify2.Notification(None,icon=ICON_PATH)

n.set_urgency(notify2.URGENCY_NORMAL) 
n.set_timeout(10000) 
  
for newsitem in newsitems: 
    n.update(newsitem['title'], newsitem['description']) 
    n.show() 
    time.sleep(15) 