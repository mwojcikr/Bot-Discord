
def handle_response(message) -> str:

    lmsg = message.lower()

    if lmsg == "hi":
        return "Hello"
    
    elif lmsg =="help":
        return f"""
Here's a list of commands :

!update -> sends links of new videos added by selected channels to discord channel called #youtube and posts from facebook to channel facebook ( in progress)\n
!facebook -> sends public posts from chosen websites to discord channel called #facebook (work in progress, 'Page Public Content Access' required)\n
!getvids -> sends links of new videos added by selected channels to discord channel #youtube\n
!getquote -> sends a quote to #quotes channel\n
"""
    else:
        return ''