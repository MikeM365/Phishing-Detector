\# Phishing Email Detector



This project is a command-line tool that uses a machine learning model to classify emails or text messages as either legitimate or a phishing attempt.



\## Features



\- Uses a pre-trained Support Vector Machine (SVM) model.

\- Analyzes text content to predict the likelihood of phishing.

\- Simple and easy-to-use command-line interface.



\## Setup and Installation



To run this project locally, follow these steps:



1\.  \*\*Clone the repository:\*\*

&nbsp;   ```

&nbsp;   git clone https://github.com/MikeM365/Phishing-Detector.git

&nbsp;   ```

2\.  \*\*Navigate to the project directory:\*\*

&nbsp;   ```

&nbsp;   cd phishing-detector

&nbsp;   ```

3\.  \*\*Create and activate a virtual environment:\*\*

&nbsp;   ```bash

&nbsp;   python -m venv venv

&nbsp;   source venv/Scripts/activate

&nbsp;   ```

4\.  \*\*Install the required packages:\*\*

&nbsp;   ```

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



\## Usage



Once the setup is complete, you can run the detector with the following command:



python phishing\_detector.py



The script will then process its hardcoded test emails and print the predictions.



\## Built With



\- \[Python](https://www.python.org/)

\- \[Scikit-learn](https://scikit-learn.org/)

\- \[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

\- \[Requests](https://requests.readthedocs.io/en/latest/)



