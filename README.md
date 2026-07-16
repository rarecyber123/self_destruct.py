 ### Self-Destruct Message

  Small CLI tool jo koi bhi message encrypt kr k " self destructing code " bana deta hai.
 Matlab message ek baar read hone ke baad ya time limit khatam hote hi khud delete ho jata hai.
 
Mai ne ye bnaya kyu k normal messaging apps mein "disappearing messages" hoti hain lekin unka backend hum dekh nahi sakte. 


 ## Ye Karta Kya Hai


Tum ek message likhte ho
Tool usay encrypt kar deta hai aur ek unique code deta hai
Tum wo code kisi ko bhejte ho (WhatsApp, email, jo bhi)
Wo insaan wo code use kar ke message decrypt kar sakta hai — sirf ek baar
Ya to read hone ke baad, ya expire time (default 24 hours) ke baad, message hamesha ke liye delete ho jata hai


Dobara koi try kare us code se to error milega — "

 ## Install

bashpip install cryptography

Kaise Chalayen

  ## Message banane ke liye:

bashpython self_destruct.py --create

Ye tumse message maangega aur ek code de dega, jese: SD-7f3ka9


 ## Message read karne ke liye:

bashpython self_destruct.py --read SD-7f3ka9

Message ek dafa dikhega, uske baad wo automatically system se delete ho jayega.

Expiry time change karna ho:

bashpython self_destruct.py --create --expires 1

# (1 ghante mein expire ho jayega)


 ## Kaise Kaam Karta Hai (Technical)


Fernet symmetric encryption (cryptography library) use hoti hai
Har message ka apna encryption key hota hai, jo message ke sath hi generate hota hai
Messages ek local SQLite database mein store hote hain (messages.db)
Jese hi message read ho ya time khatam ho, us row ko database se permanently delete kar diya jata hai — recovery possible nahi


## For learning purpose only 



