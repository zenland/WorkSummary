import rados,sys

cluster=rados.Rados(conffile='ceph/ceph-cluster/ceph.conf')
print "\nlibrados version: "+str(cluster.version())
print "Will attempt to connect to: "+str(cluster.conf_get('mon initial members'))

cluster.connect()
print "\nCluster ID: "+cluster.get_fsid()

print "\n\nCluster Statistics"
print "======================"
cluster_stats=cluster.get_cluster_stats()

for key,value in cluster_stats.iteritems():
    print key,value
