class Interval():
    def __init__(self, l, h):
        self.low = l
        self.high = h

    def overlap(self, interval2):
        if self.low <= interval2.high and interval2.low <= self.high:
            return True
        return False

class ITNode():
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None


def insert(root, i):
    if root == None:
        return ITNode(i)
    l = root.interval.low
    if i.low < l:
        root.left = insert(root.left,i)
    else:
        root.right = insert(root.right,i)

    if root.max < i.high:
        root.max = i.high

    return root


def overlapSearch(root, i):
    if root is None:
        return None

    if root.interval.overlap(i):
        return root.interval

    if root.left is not None and root.left.max >= i.low:
        return overlapSearch(root.left, i)

    return overlapSearch(root.right, i)

def inOrder(root):
    if root is None:
        return

    inOrder(root.left)

    print("[%s, %s] max = %s" % (root.interval.low,root.interval.high,root.max))

    inOrder(root.right)

intervals = [Interval(15,20),Interval(10,30),Interval(17,19),Interval(5,20),Interval(12,15),Interval(30,40)]
root = ITNode(intervals[0])
for i in range(1,len(intervals)):
    insert(root,intervals[i])

print("Inorder traversal of constructed Interval Tree:")
inOrder(root)

x = Interval(6,7)
print("Searching for interval [%s,%s]" % (x.low,x.high))
res = overlapSearch(root,x)
if res is None:
    print("No overlapping interval")
else:
    print("Overlaps with [%s,%s]" % (res.low, res.high))