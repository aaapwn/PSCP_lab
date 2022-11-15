"""Ping"""
def findip(info):
    """find ip adress"""
    if info.count("[") >= 1:
        start = info.index("[")
        stop = info.index("]")
        ipadress = info[start+1:stop]
    else:
        start = info.index(" ")
        stop = info.index("w")
        ipadress = info[start+1:stop-1]
    return ipadress

def countreceived(reply1, reply2, reply3, reply4):
    """count Received"""
    received = 0
    lost = 0
    if reply1.count("Reply") == 1:
        received += 1
    else:
        lost += 1
    if reply2.count("Reply") == 1:
        received += 1
    else:
        lost += 1
    if reply3.count("Reply") == 1:
        received += 1
    else:
        lost += 1
    if reply4.count("Reply") == 1:
        received += 1
    else:
        lost += 1
    return received, lost

def fingping(reply1, reply2, reply3, reply4):
    """find all ping"""
    def findtime(reply):
        """find where is ping"""
        if reply.count("time=") == 1:
            start = reply.index("time=")
            stop = reply.index("ms")
            time = reply[start+5:stop]
            if time == "<1":
                time = 0
            return time
        else:
            return 0
    time1 = findtime(reply1)
    time2 = findtime(reply2)
    time3 = findtime(reply3)
    time4 = findtime(reply4)
    return time1, time2, time3, time4

def sorttime(time1, time2, time3, time4):
    time1, time2, time3, time4 = int(time1), int(time2), int(time3), int(time4)
    if time2 < time1:
        time2, time1 = time1, time2
    if time3 < time1:
        time3, time1 = time1, time3
        time2, time1 = time1, time2
    elif time3 < time2:
        time3, time2 = time2, time3

    if time4 < time1:
        time1, time4 = time4, time1
        time2, time4 = time4, time2
        time3, time4 = time4, time3
    elif time4 < time2:
        time2, time4 = time4, time2
        time3, time4 = time4, time3
    elif time4 < time3:
        time4, time3 = time3, time4
    return time1, time2, time3, time4

def main():
    """Ping"""
    input()
    input()
    info = input()
    reply1 = input()
    reply2 = input()
    reply3 = input()
    reply4 = input()
    ipadress = findip(info)
    received, lost = countreceived(reply1, reply2, reply3, reply4)
    time1, time2, time3, time4 = fingping(reply1, reply2, reply3, reply4)
    time1, time2, time3, time4 = sorttime(time1, time2, time3, time4)
    loss_1 = int(lost*100/4)
    loss = str(loss_1) + "%"
    #  output
    print("Ping statistics for %s:" %ipadress)
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%s loss)," %(received, lost, loss))
    if lost != 4:
        avg = int((time1+time2+time3+time4)/received)
        print("Approximate round trip times in milli-seconds:")
        if lost == 0:
            print("    Minimum = %dms, Maximum = %dms, Average = %dms" %(time1, time4, avg))
        elif lost == 1:
            print("    Minimum = %dms, Maximum = %dms, Average = %dms" %(time2, time4, avg))
        elif lost == 2:
            print("    Minimum = %dms, Maximum = %dms, Average = %dms" %(time3, time4, avg))
        elif lost == 3:
            print("    Minimum = %dms, Maximum = %dms, Average = %dms" %(time4, time4, avg))
main()
