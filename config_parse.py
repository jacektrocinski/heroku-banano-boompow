import argparse
import re

WORK_TYPES = ["ondemand", "precache", "any"]

def banano_public_address(string):
    p = re.compile('^(ban)_[13]{1}[13456789abcdefghijkmnopqrstuwxyz]{59}$')
    if not p.match(string):
        msg = "%r is not a valid BANANO address" % string
        raise argparse.ArgumentTypeError(msg)
    return string

class BpowClientConfig(object):

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--server', type=str, default='wss://client:client@bpow.banano.cc/mqtt', help="MQTT broker URI")
        parser.add_argument('--worker_uri', type=str, default='127.0.0.1:7000', help='URI of work server listening for RPC calls.')
        parser.add_argument('--payout', type=banano_public_address, required=True, help='Payout address.')
        parser.add_argument('--work', type=str, action='store', choices=WORK_TYPES, default="any", help='Desired work type. Options: any (default), ondemand, precache.')
        parser.add_argument('--async_mode', action='store_true', help='Request work without waiting for any results from the worker, may increase performance at the expense of using more system resources', default=False)
        parser.add_argument('--limit-logging', action='store_true', help='Log less information, keep console spam down', default=False)

        args = parser.parse_args()

        self.server = args.server
        self.worker = args.worker_uri
        self.payout = args.payout
        self.work_type = args.work
        self.async_mode = args.async_mode
        self.limit_logging = args.limit_logging
