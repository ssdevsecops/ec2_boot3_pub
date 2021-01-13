import boto3

ec2 = boto3.resource('ec2', region_name='us-west-1')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-03130878b60947df3',  
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='dev2020'
 )