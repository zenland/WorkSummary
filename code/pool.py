import rados,sys

cluster=rados.Rados(conffile='../ceph/ceph-cluster/ceph.conf')

cluster.connect()

print "\n\nPool Operations"
print "==================="
print "\nAvailables Pools"
print "-------------------"
pools=cluster.list_pools()

for pool in pools:
    print pool

print "\nCreate 'test' pool"
print "------------------"
cluster.create_pool('data')
'''
print "\nPool named 'test' exists: "+str(cluster.pool_exists('test'))
print "\nVerify 'test' Pool Exists"
print "----------------------"
pools=cluster.list_pools()
for pool in pools:
    print pool

print "\nDelete 'test' Pool"
print "--------------------------"
cluster.delete_pool('test')
print "\nPool named 'test' exists: "+str(cluster.pool_exists('test'))i
'''
