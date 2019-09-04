#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
import uuid
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator


# You should be able to connect to
# the ips of the whole cluster from the maching running the script.
# Or you'll see error like

# *** couchbase.exceptions._TimeoutError_0x17 (generated, catch TimeoutError): <Key='12', RC=0x17[Client-Side timeout exceeded for operation. Inspect network conditions or increase the timeout], Operational Error, Results=1, C Source=(src/multiresult.c,316), Tracing Output={"12": {"s": "kv:Unknown", "i": 823564440, "b": "bucket_sample", "r": "172.42.92.71:11210", "t": 2500000}}>
cluster = Cluster('couchbase://couchbase_ip')
authenticator = PasswordAuthenticator('Administrator', 'password')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('bucket_sample')

def main():
    document = {
        "key": "value",
    }

    key = str(uuid.uuid4())
    cb.upsert(key, document)
    print(key)


if __name__ == "__main__":
    main()
