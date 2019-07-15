import subprocess, configparser

print("Enter your input S3 Bucket's Credentials: ")
access_key = input("S3 Access Key: ")
secret_key = input("S3 Secret Key: ")
f = open("s3.keypair","w+")
f.write(access_key+"\n")
f.write(secret_key)
f.close()
endpoint = input("S3 endpoint (e.g. s3.amazonaws.com): ")
region = input("S3 Region: ")
bucket = input("Bucket Path: ")
hostname = input("iRODS Hostname (irods@*hostname*): ")
resource = input("New S3 Cacheless Resource Name: ")

subprocess.check_call(['/etc/irods/automated_ingest/scanner.sh', endpoint, region, bucket, hostname, resource])
