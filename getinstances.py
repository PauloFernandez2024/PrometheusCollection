import requests

class GetInstances():

    def __init__(self, prometheus_url):
        self.prometheus_url = prometheus_url

    def get_prometheus_instances(self):
        try:
            response = requests.get(f"{self.prometheus_url}/api/v1/targets")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            instances = []
            for target in data['data']['activeTargets']:
                instance = target['labels'].get('instance', 'N/A')
                job = target['labels'].get('job', 'N/A')
                scrapeInterval = target.get('scrapeInterval', 'N/A')
                instances.append((job, instance, scrapeInterval))

            return instances
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Prometheus: {e}")
            return []
