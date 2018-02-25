import itchat
import random
import time

random.seed()

# Define a decorator to help make count a "static local variable"
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@itchat.msg_register(itchat.content.TEXT, isFriendChat = True, isGroupChat = False, isMpChat = False)
@static_vars(count = 0)
def text_reply(msg):

    print("from:  " + msg.fromUserName)
    print("to:    " + msg.toUserName)
    print("text:  " + msg.content)

    if msg.fromUserName == itchat.originInstance.storageClass.userName: return
        # Avoid replying to messages sent by yourself
    if msg.content == "[抱拳]"*text_reply.count: 
        # Avoid endless mutual admire in case your friend is also using MutualAdmire
        print("Enough admiration! ")
        text_reply.count = 0
        return

    text_reply.count = msg.content.count("[抱拳]")
    if text_reply.count == 0: return
    
    delay = 1 + 2*random.random() # Set a random 1-3 seconds' delay
    time.sleep(delay) # This is to dodge anti-robot check

    print("delay: " + str(delay) + " sec(s)")
    print("count: " + str(text_reply.count) + '*"[抱拳]"')

    msg.user.send("[抱拳]"*text_reply.count)
    return

itchat.auto_login(hotReload = True)
itchat.run()

pass
