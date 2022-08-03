## File structure and purpose
- `speech-infra.sh` - Bash script to trigger creation of a speech resource, with a storage container.
	- One must have a `sub.env` file in the same directory, with `SUB_ID` and `EMAIL_ID` variables.
	- The audio files need to be manually loaded into the storage container. Recommendation: Storage
	  Explorer.
- `batch_request.py` - File to trigger a batch request against the speech resources.
- `prepping-data` - Folder that contains a number of scripts to aid data cleansing and normalization.
