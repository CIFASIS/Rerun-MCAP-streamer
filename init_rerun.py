import rerun as rr
import sys

memory_limit = sys.argv[1]

rr.init("batch_example")
rr.spawn(memory_limit=memory_limit, connect=False)
