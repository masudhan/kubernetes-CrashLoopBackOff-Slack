from kubernetes import client, config
import requests
import pandas as pd

def k8s_client():
    # Configuration for accessing the K8s Cluster
    config.load_kube_config("~/.kube/config")
    # Create and return an instance of the CoreV1Api class
    return client.CoreV1Api()

k = k8s_client()

def getpodstatus(pod):
    return pod.status.phase

def run(**kwargs):
    namespace = kwargs.get('namespace')
    podlist = k.list_namespaced_pod(namespace= namespace)
    data = []
    try:   
        for item in podlist.items:
            pod = k.read_namespaced_pod_status(namespace= namespace, name=item.metadata.name)
            if(pod.status.container_statuses[0].state.waiting):
                if (pod.status.container_statuses[0].state.waiting.reason == "CrashLoopBackOff"):
                    data.append([pod.metadata.name,pod.status.container_statuses[0].state.waiting.reason,pod.status.container_statuses[0].last_state.terminated.message])
        df = pd.DataFrame(data=data, columns=["Pod_Name", "Pod_Status", "Reason, if any"])
        markdown_table = df.to_markdown()
        print(markdown_table)
        json_data = {
            'text': "```\n" + markdown_table + "\n```",
        }
        response = requests.post('<SLACK-WEBHOOK>', json=json_data)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
    except:
        print("error occured, retrying")
        run(namespace="<NAMESPACE>")

run(namespace="<NAMESPACE>")
