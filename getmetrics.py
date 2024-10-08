import requests

class GetMetrics():


    def __init__(self, prometheus_url, instance, job):
        self.prometheus_url = prometheus_url
        self.instance = instance
        self.job = job


    def get_metrics_for_instance(self):
        try:
            # Construct the query to get all metrics for the specified instance
            query = f'{{instance="{self.instance}", job="{self.job}"}}'
    
            # Endpoint to fetch metrics
            response = requests.get(f"{self.prometheus_url}/api/v1/query", params={'query': query})
            response.raise_for_status()  # Raise an error for bad responses
    
            # Parse the JSON response
            data = response.json()
    
            # Check if there are any metrics returned
            if data['data']['result']:
                metrics = data['data']['result']
                return metrics
            else:
                print(f"No metrics found for instance: {instance}")
                return []
    
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Prometheus: {e}")
            return []
