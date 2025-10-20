"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""
def grant_access(verified, user_id, flags):
    if verified and (user_id & 1 == 0) and (flags & 0b111 != 0):
        print("Access granted.")
    else:
        print("Access denied.")
grant_access(verified=True, user_id=102, flags=0b100)
grant_access(verified=True, user_id=103, flags=0b100)
grant_access(verified=False, user_id=102, flags=0b100)  
grant_access(verified=True, user_id=102, flags=0b000)   
