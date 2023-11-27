# CI-Monitoring-Automation



### Overview

The ci-monitoring-automation Repository is a collection of Python scripts designed to automate monitoring of Continuous Integration (CI) system workflows. These scripts facilitate the retrieval and analysis of information related to coreOS CI builds, offering developers the flexibility to gather data of builds run for the current day or within a specified date range.

### Installation

```
git clone https://github.com/SurajGudaji/ci-monitoring-automation.git
cd ci-monitoring-automation
pip install virtualenv
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Usage

1. **CI_DailyBuildUpdate.py:** The CI_DailyBuildUpdates.py script will fetch and display information of the all builds that ran on the CI system for the current day.  

    1. Brief Information: Displays Build type, Job ID, Install status, Lease and total e2e testcase failures.

        ```python3 CI_DailyBuildUpdates.py --info_type brief```

    2. Detailed Information: Dispalys Job ID, Job link, Lease quota, Nighlty image, Node status, Check for Node crash, list of failed testcases.  

        ```python3 CI_DailyBuildUpdates.py --info_type detailed```



2. **CI_JobHistory.py:** The CI_JobHistory.py is a interactive script which allows user to query a specific information from all builds that ran on the CI system within a given date range.  
    ```python3 CI_JobHistory.py```


3. **config.json:** The config.json file has the ci names and ci links in key value pairs which will be used by the scripts to get the builds, new CI's can be easily integrated by adding the ci name and ci link in the config.json file.
