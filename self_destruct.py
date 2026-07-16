
"""
Self-Destruct Message
----------------------
Message encrypt karke ek code deta hai. Wo code sirf ek baar
use ho sakta hai (ya expiry time khatam hone tak) — uske baad
message database se permanently delete ho jata hai.

Usage:
    python self_destruct.py --create
    python self_destruct.py --create --expires 1
    python self_destruct.py --read SD-xxxxxx
"""

