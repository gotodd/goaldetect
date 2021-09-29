RFC goal detection

sample JSON mesage sent over wire to Roborio:
```
{"type":"targets","message":"{\"capturedAgoMs\":45,\"targets\":[{\"y\":0.24827434210216298,\"z\":-0.07189401450834836}]}"}
```
currently, app is running in landscape mode. Y is aross the long side of the
phone, and Z is across the short edge of the phone. If the target is at the top
of the screen near the top notch, Y is close to -0.5. At the bottom Y is close
to 0.5. Z is close to 0.36 when at the right edge, and -0.36 at the left edge,
when holding the phone in portrait mode.
```
---------^---------
        *(Y is -0.5,Z is 0)






*(Y is 0, Z is 0.36)








        *(Y is 0.5, Z is 0)
--------------------
      ^   O   Q
```
