import metric_pb2

my_metric = metric_pb2.Metric()
my_metric.name = 'sys.cpu'
my_metric.type = 'gauge'
my_metric.value = 'gauge'
my_metric.tags.extend(['my_tag', 'foo:bar'])

with open('out.bin', 'wb') as f:
    f.write(my_metric.SerializeToString())
    