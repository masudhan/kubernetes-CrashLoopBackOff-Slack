#### Requirements and how to run?
`Kubernetes config file in ~/.kube/config  (if you want you can change the location, but this is the default location)`

1. Python 3.7 or later (I have 3.7 so yeah..)
2. `pip3.7 install kubernetes`
3. `pip3.7 install pandas`
4. Replace `SLACK-WEBHOOK` with actual slack webhook in quotes
5. Replace `NAMESPACE` with actual name space like `staging` or `production` in quotes
6. In command line - `python3 crashloop.py`

#### Output
On slack, notification will be 👇

|    | Pod_Name                                      | Pod_Status       | Reason, if any   |
|---:|:----------------------------------------------|:-----------------|:-----------------|
|  0 | facebook-service-218b115bc4c-c9jdx            | CrashLoopBackOff |                  |
|  1 | google-service-distrubuter-4884c422b4-f4pxw   | CrashLoopBackOff |                  |
