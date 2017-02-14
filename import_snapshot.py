import logging
import sys
import pdb
from pprint import pprint
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
#logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)

EC2_ACCESS_ID = 'Your Access Key'
EC2_SECRET_KEY = 'Your Secret Key'

EC2Driver = get_driver(Provider.EC2)
driver = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)
disk_container = [{'Description': 'amisstea-test2',
                  'Format': 'raw',
                  'UserBucket': {
                    'S3Bucket': 'amisstea-test',
                    'S3Key': 'rhel-server-ec2-7.3-6.x86_64.raw'
                  }}]
#pdb.set_trace()
obj = driver.ex_import_snapshot(disk_container=disk_container)
pprint(obj)
