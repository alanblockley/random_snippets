### This is just a random snip from something I wrote quickly. 
### If you need a list of regions to process later in a suitable format. 
### e.g. Looping through regions for automation. 

import boto3

def getRegions():

    regions = []

    ec2_client = boto3.client('ec2')
    describe_regions = ec2_client.describe_regions()
    for region in describe_regions['Regions']:
        regions.append(region['RegionName'])

    return regions 
