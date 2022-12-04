import os
import logging
import boto3
from sagemaker import get_execution_role, Session

logging.basicConfig(level=logging.INFO)


# TODO: Error in the download of file from S3. Check this out
AWS_REGION = "us-east-1"
sagemaker_session = Session(boto3.session.Session(region_name=AWS_REGION))
logging.info(f"REGION_NAME: {sagemaker_session.boto_region_name}")

sagemaker_execution_role = get_execution_role(sagemaker_session=sagemaker_session)

s3 = boto3.resource('s3')


def prepare_data():
    # GET DATASET FROM SCIKIT-LEARN
    # df = datasets.fetch_california_housing(as_frame=True).frame

    # TODO:
    # 1. Fetch the dataset from the S3
    # 2. Doing all the preprocessing steps
    # 3. Save all the results content to the S3
    download_s3_folder(bucket_name="face-spoofing-bucket",
                       s3_folder="live")
    download_s3_folder(bucket_name="face-spoofing-bucket",
                       s3_folder="fake")
    logging.info("Downloaded the data from S3")
    logging.info(f"Directories: {os.listdir()}")
    # SAVE DATASET INTO CSV FILE
    # logging.info("SAVE DATASET INTO CSV FILE")
    # df.to_csv(f"{os.environ['output_folder']}/housing.csv", sep=",", index=False)


def download_s3_folder(bucket_name, s3_folder, local_dir=None):
    """
    Download the contents of a folder directory
    Args:
        bucket_name: the name of the s3 bucket
        s3_folder: the folder path in the s3 bucket
        local_dir: a relative or absolute directory path in the local file system
    """
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = obj.key if local_dir is None \
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        bucket.download_file(obj.key, target)


if __name__ == "__main__":
    prepare_data()
