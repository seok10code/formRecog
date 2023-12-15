from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

import os
import json
import requests

# from dotenv import load_dotenv
# load_dotenv("credentials.env",override=True)



FORM_RECOGNIZER_KEY="87fa"
FORM_RECOGNIZER_ENDPOINT="https://formtestswsw.com/"

def get_blob_url():
    STORAGE_CONSTR = "Default"
    SOURCE_NAME = "formcontianer"
    FILE_NAME = "20231201_pdf_to_txt.pdf"
    # FILE_NAME = "test01.pdf"
    sas=""
    container = ContainerClient.from_connection_string(
         conn_str=STORAGE_CONSTR,
         container_name = SOURCE_NAME,
        #  credential=sas
    )

    blob_list = container.list_blobs()
    blob_url = container.url

    for blob in blob_list:
        if blob.name == FILE_NAME:  
            formUrl = blob_url+"/"+blob.name
    return formUrl



def analyze_read():
    formUrl = get_blob_url()

    document_analysis_client = DocumentAnalysisClient(
        endpoint=FORM_RECOGNIZER_ENDPOINT, credential=AzureKeyCredential(FORM_RECOGNIZER_KEY)
    )
    print(formUrl)
    print('='*60)
    poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-read", formUrl)
    result = poller.result()

    # print("Document contains contestn:" , result.content)
    with open("/mnt/c/Users/김석원/Desktop/python_script/pdf_file_test.txt", "w") as text_file:
         text_file.write(result.content+'\n\n\n\n\n')
    # for page in result.content:
        # with open("/mnt/c/Users/김석원/Desktop/python_script/pdf_file.txt", "w") as text_file:
            # text_file.write(f"{page_num}:" + f"{page}" + "\n")
        # print("="*70)
        # print(page)


if __name__ == "__main__":
	analyze_read()
