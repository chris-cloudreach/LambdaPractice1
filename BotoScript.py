import json
import boto3
def handler(event, context):
    s3_obj =boto3.client('s3') #creating object for accessing s3

    s3__pet_obj = s3_obj.get_object(Bucket='my-first-lambdabucket-194694014750', Key='PetDb.json')
    s3__pet_data = s3__pet_obj['Body'].read().decode('utf-8')


    s3_pet_list=json.loads(s3__pet_data)
    print("json loaded data")
    

    lo_pet_dict=next(item for item in s3_pet_list if item["name"] == event.PetName)
    print(lo_pet_dict)

    return lo_pet_dict.get('favFoods')
    