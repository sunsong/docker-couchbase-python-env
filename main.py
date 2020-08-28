#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
import uuid
from couchbase.cluster import Cluster, ClusterOptions, QueryOptions
from couchbase_core.cluster import PasswordAuthenticator


# The following are deprecated note
# ===================================================================
# You should be able to connect to
# the ips of the whole cluster from the maching running the script.
# Or you'll see error like
#
# *** couchbase.exceptions._TimeoutError_0x17 (generated, catch TimeoutError): <Key='12', RC=0x17[Client-Side timeout exceeded for operation. Inspect network conditions or increase the timeout], Operational Error, Results=1, C Source=(src/multiresult.c,316), Tracing Output={"12": {"s": "kv:Unknown", "i": 823564440, "b": "bucket_sample", "r": "172.42.92.71:11210", "t": 2500000}}>
#
# ===================================================================

# For couchbase version 3
cluster = Cluster(
    'couchbase://couchbase_ip',
    ClusterOptions(
        PasswordAuthenticator('Administrator', 'password')
    )
)

bucket = cluster.bucket('bucket_sample')
coll = bucket.default_collection()


def main():
    document = {
        "key": "value",
    }

    key = str(uuid.uuid4())
    coll.upsert(key, document)
    print(key)


if __name__ == "__main__":
    main()
