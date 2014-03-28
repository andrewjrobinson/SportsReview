''' 
NOTE1: Close all SportsReview applications before editing as your changes may be lost.
NOTE2: File is regenerated upon changing a setting within GUI.  Only this DocString will be kept.

Timing:
-- (past) -- time -- (present) -->
----KKKKKKKKKKDDDDDDDDDDEEEEE
                       /\ captured frame
             /\ on-screen frame
K = keepalive
D = delay
E = extend




Settings:
- delay:     float, seconds between capturing a frame to displaying it when in playback mode.
- keepalive: float, seconds to keep frames for after they are displayed (i.e. used for backup in paused mode)
- extend:    float, seconds to keep recording frames for when pausing

'''
settings = {'delay': 2.0, 'extend': 1.0, 'keepalive': 2.0}
