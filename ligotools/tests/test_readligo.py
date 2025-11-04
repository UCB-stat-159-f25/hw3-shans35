from ligotools import readligo as rl
import numpy as np

def test_dq_channel_to_seglist():
    # Create a simple 1Hz channel with two valid segments
    ch = np.array([0, 0, 1, 1, 1, 0, 1, 1, 0]) # create an array for a channel with two segments (slices 2-5 and 6-8)
    segs = rl.dq_channel_to_seglist(ch, fs=1)
    assert segs[0].start == 2
    assert segs[0].stop == 5
    assert segs[1].start == 6
    assert segs[1].stop == 8
    assert len(segs) == 2

def test_segmentlist_from_list():
    segs = rl.SegmentList([[200, 300], [400, 500], [700, 800]])
    assert len(segs.seglist) == 3
    assert segs[0] == [200, 300]