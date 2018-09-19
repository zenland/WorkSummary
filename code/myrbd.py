import rados
import rbd

cluster = rados.Rados(conffile='/etc/ceph/ceph.conf')
cluster.connect()
ioctx = cluster.open_ioctx('rbd')

rbd_inst = rbd.RBD()
size = 1024**3
image_name = "foo"
rbd_inst.create(ioctx, image_name, size)

image = rbd.Image(ioctx, image_name)
data = 'foo' * 100
image.write(data, 0)

image.close()
ioctx.close()
cluster.shutdown()
