import rerun as rr
import sys

recording_id = sys.argv[1]
memory_limit = sys.argv[2]

rr.init(recording_id)
rr.spawn(memory_limit=memory_limit, connect=False)
