import rados,sys

cluster=rados.Rados(conffile='../ceph/ceph-cluster/ceph.conf')

cluster.connect()
if not cluster.pool_exists('data'):
    cluster.create_pool('data')

#WRITING, READING AND REMOVING OBJECTS
ioctx=cluster.open_ioctx('data')

print "\nWriting object 'hw' with contents 'Hello World!' to pool 'data'."
ioctx.write_full("hw","Hello World!")

print "\n\nContents of object 'hw' \n------------------------\n"
print ioctx.read("hw")

#WRITING AND READING XATTRS

print "\n\nWriting XATTR 'lang' with value 'en_US' to object 'hw'"
ioctx.set_xattr("hw","lang","en_US")

print "\n\nGetting XATTR 'lang' from object 'hw'\n"
print ioctx.get_xattr("hw","lang")

#LISTING OBJECTS
ioctx.write_full("test","my hello world!")
object_iterator=ioctx.list_objects()

while True:
    try:
        print "\n\n listing objects\n"
        rados_object=object_iterator.next()
        print "Object contents ="+rados_object.read()
    except StopIteration :
        break

print "\nRemoving object 'hw'"
ioctx.remove_object("hw")

