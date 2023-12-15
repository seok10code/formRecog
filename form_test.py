from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

import os
import json
import requests

# from dotenv import load_dotenv
# load_dotenv("credentials.env",override=True)



FORM_RECOGNIZER_KEY="879c3234abea403ca50dc047e85051fa"
FORM_RECOGNIZER_ENDPOINT="https://formtestswsw.cognitiveservices.azure.com/"

def get_blob_url():
    STORAGE_CONSTR = "DefaultEndpointsProtocol=https;AccountName=uploadfiletesttestsw;AccountKey=fZZ0DCbO3C3pXAGDHZKzQ+XcXp2OQdl5gc2ysrLTP4deFbZedIMylcggLNpPNcgqEXUXj044eC66+ASttOSzlA==;EndpointSuffix=core.windows.net"
    SOURCE_NAME = "formcontianer"
    FILE_NAME = "20231201_pdf_to_txt.pdf"
    # FILE_NAME = "test01.pdf"
    sas="sp=racwdymeop&st=2023-11-28T02:15:13Z&se=2023-12-08T10:15:13Z&spr=https&sv=2022-11-02&sr=b&sig=cAzuKe15FAWNbm%2B%2B3CcdGf6VMg0hgklzhLQFcqUOS3k%3D"
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