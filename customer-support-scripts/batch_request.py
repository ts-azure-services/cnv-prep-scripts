import os
import csv
import time
import random
import requests
import json
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

class speechMethods:
    def __init__(self):
        self.access_variables = self.load_variables()
        self.sample_wav_file = './data-feeds/wav-files/martha.wav'
        self.text_to_speech_file = './data-feeds/gettysburg-short.txt'
        self.location = self.access_variables['speech_location']
        self.transcription_path = f'https://{self.location}.api.cognitive.microsoft.com/speechtotext/v3.0/transcriptions'
        self.headers = {'Content-Type': 'application/json','Ocp-Apim-Subscription-Key':self.access_variables['speech_key']}

    # Load sub, tenant ID variables 
    def load_variables(self):
        """Load access variables"""
        env_var=load_dotenv('./variables.env')
        auth_dict = {
                "speech_key":os.environ['SPEECH_KEY'],
                "speech_endpoint":os.environ['SPEECH_ENDPOINT'],
                "speech_location":os.environ['SPEECH_LOCATION'],
                "blob_container_sas_url":os.environ['BLOB_CONTAINER_SAS_URL']
                }
        return auth_dict


    def send_batch_transcribe_request(self):
        body = {
                #"contentUrls":[<specific SAS URL to file>],
                 "contentContainerUrl": self.access_variables['blob_container_sas_url'],
          "properties": {
            "diarizationEnabled": "false",
            "wordLevelTimestampsEnabled": "true",
            "punctuationMode": "DictatedAndAutomatic",
            "profanityFilterMode": "Masked"
          },
          "locale": "en-US",
          "displayName": "Transcription using default model for en-US"}

        response = requests.post(self.transcription_path, headers=self.headers, json=body)
        status, reason, resp_headers = response.status_code, response.reason, response.headers
        print(f"response status code: {status}")
        print(f"response status: {reason}")
        print(f"response headers: {resp_headers}")
        resp_headers_dict = dict(resp_headers)
        request_id = resp_headers_dict['Location'].split('/transcriptions/')[1]
        print(f'Request ID: {request_id}')
        return request_id

    def get_transcript_links(self, request_id=None):
        """Get transcription result; do this manually in an ipython terminal"""

        # Get request id, and use this to pulse a while loop
        path = self.transcription_path + '/' + str(request_id) + '/files'
        response = requests.get(path, headers=self.headers)
        status, reason, resp_headers, resp_content = response.status_code, response.reason, response.headers, response.content
        print(f"response status code: {status}")
        resp_content_json = json.loads(resp_content.decode('utf-8'))

        if resp_content_json['values'] == []:
            print('Pinged the service, but seems request might still be processing......')
            return False
        else:
            # Processing done. 
            # Proceed with querying each enumeration query link. Capped at 100, per payload.
            responses = []
            responses.append(resp_content_json['values']) #store the first pass
            path = resp_content_json['@nextLink']
            while path:
                print(f"Current path: {path}")
                response = requests.get(path, headers=self.headers)
                resp_content = response.content
                resp_content_json = json.loads(resp_content.decode('utf-8'))
                responses.append(resp_content_json['values'])
                try:
                    path = resp_content_json['@nextLink']
                except:
                    break

            # Iterate through all possibilities
            if responses:
                print(f"Returned response count: {len(responses)}")
                transcript_links = []
                for response in responses:
                    for i,v in enumerate(response):
                        contentUrl = v['links']['contentUrl']
                        transcript_links.append(contentUrl)

            # Write out links to query
            print(f"Outputting {len(transcript_links)} transcript links to a file...")
            with open('./links.txt', 'w') as f:
                for transcript in transcript_links:
                    f.write(transcript + '\n')
            return True

    def query_transcript(self, link=None):
        """Query for transcript from provided link"""

        # Check if file exists, else create an empty list
        try:
            transcripts = existing_details('./transcripts.csv')
            existing_links = [x['content_link'] for x in transcripts]
        except:
            transcripts = []
            existing_links = []

        # You have to query each link to check if the content link returned
        # is not already part of the data. If it is, then you ignore it.
        # Might choose randomly, so that you cover more area.

        # Check if link does not already have data
        if link not in existing_links:
            sleep_time = random.randint(1,4)
            print(f"Doze for {sleep_time} seconds...")
            time.sleep(sleep_time)
            try:
                audio_file_response = requests.get(link, headers=self.headers)
                if audio_file_response.status_code == 200:
                    # Check if the summary report
                    resp_content = audio_file_response.content
                    if "successfulTranscriptionsCount" in str(resp_content):
                        print("Summary report result...")
                    else:
                        resp_content_json = json.loads(resp_content.decode('utf-8'))
                        source_file_path = resp_content_json['source']
                        try:
                            lexical = resp_content_json['combinedRecognizedPhrases'][0]['lexical']
                        except:
                            lexical = 'No lexical value'

                        try:
                            display = resp_content_json['combinedRecognizedPhrases'][0]['display']
                        except:
                            display = 'No display value'

                        def audio_filename(x=None):
                            """Small function to parse out filename"""
                            x = x.split('.wav')
                            if len(x)==2:
                                y = x[0].split('/')
                                filename = y[-1:][0]
                            return filename

                        filename = audio_filename(x=source_file_path)
                        temp_dict = {'source_file_path': source_file_path,
                                'content_link': link,
                                'filename': filename,
                                'lexical': lexical,
                                'display': display}
                        transcripts.append(temp_dict)
            except Exception as e:
                print(e)
                write_out_results(transcripts)
        else:
            print('Link already in the dataset...')

        # Once out of the loop, write results
        write_out_results(transcripts)

def existing_details(source=None):
    """Read in existing transcripts into a list of dictionaries"""
    existing_list = []
    with open(source,'r') as f:
        data = csv.DictReader(f)
        for row in data:
            existing_list.append(row)
    return existing_list

def write_out_results(transcripts=None):
    """Write out results to a CSV file"""
    print(f"Length of transcript list: {len(transcripts)}")
    with open('transcripts.csv', 'w', newline='') as csvfile:
        fieldnames = ['source_file_path', 'content_link', 'filename', 'lexical', 'display']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for transcript in transcripts:
            writer.writerow(transcript)

if __name__ == "__main__":
    t = speechMethods()

    ## NORMAL BATCH REQUEST AND PROCESSING
    #request_id = t.send_batch_transcribe_request()
    #print('Sleeping for 5 seconds...')
    #time.sleep(5)

    ## Request status
    #status_request = False
    #while status_request == False:
    #    status_request = t.get_transcript_links(request_id)
    #    print('Request still processing... Waiting another 30 seconds.')
    #    time.sleep(30)

    ## QUERY WITH A REQUEST ID
    #request_id = "f6968b4c-9c9d-4b03-982d-4e71736c03e8"

    ## Request status
    #status_request = False
    #while status_request == False:
    #    status_request = t.get_transcript_links(request_id)


    """
    Note: Once you have the links generated, don't run the above again since that
    will change the link definitions, and not allow you to run the following code consistently.
    """

    # Open link file, and iterate through pending links
    with open('./links.txt', 'r') as f:
        links = f.readlines()
        links = [x.replace('\n', '') for x in links]

    for link in links:
        t.query_transcript(link=link)
