 ### Self-Destruct Message

  Small CLI tool jo koi bhi message encrypt kr k " self destructing code " bana deta hai.
 Matlab message ek baar read hone ke baad ya time limit khatam hote hi khud delete ho jata hai.
 
mai ne ye bnaya kyu k normal messaging apps mein "disappearing messages" hoti hain lekin unka backend hum dekh nahi sakte. 

Logic and how it works describe below :

Ye Karta Kya Hai


Tum ek message likhte ho
Tool usay encrypt kar deta hai aur ek unique code deta hai
Tum wo code kisi ko bhejte ho (WhatsApp, email, jo bhi)
Wo insaan wo code use kar ke message decrypt kar sakta hai — sirf ek baar
Ya to read hone ke baad, ya expire time (default 24 hours) ke baad, message hamesha ke liye delete ho jata hai


Dobara koi try kare us code se to error milega — "
