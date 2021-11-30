import json
import boto3
def handler(event, context):
    s3_obj =boto3.client('s3',aws_access_key_id="*********",aws_secret_access_key="*********") #creating object for accessing s3

    s3_pet_obj = s3_obj.get_object(Bucket='my-first-lambdabucket-194694014750', Key='PetDb.json')
    s3__pet_data = s3_pet_obj['Body'].read().decode('utf-8')


    s3_pet_list=json.loads(s3__pet_data)
    print("json loaded data")
    

    lo_pet_dict=next(item for item in s3_pet_list['pets'] if item["name"] == event["PetName"])
    

    return lo_pet_dict.get('favFoods')
    