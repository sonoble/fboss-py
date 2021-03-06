#
# Autogenerated by Thrift Compiler (1.0.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class fb_status:
  """
  Common status reporting mechanism across all services
  """
  DEAD = 0
  STARTING = 1
  ALIVE = 2
  STOPPING = 3
  STOPPED = 4
  WARNING = 5

  _VALUES_TO_NAMES = {
    0: "DEAD",
    1: "STARTING",
    2: "ALIVE",
    3: "STOPPING",
    4: "STOPPED",
    5: "WARNING",
  }

  _NAMES_TO_VALUES = {
    "DEAD": 0,
    "STARTING": 1,
    "ALIVE": 2,
    "STOPPING": 3,
    "STOPPED": 4,
    "WARNING": 5,
  }

