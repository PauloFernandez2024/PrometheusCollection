#!/usr/bin/env python3

import sys
import getinstances
import getmetrics


def main(prometheus_url):
    #prometheus_url = "http://172.16.10.208:9091"
    f = open("collection.log", "w")
    instances = getinstances.GetInstances(prometheus_url)
    for job, instance, scrapeInterval in instances.get_prometheus_instances():
        print(f"Job: {job}, Instance: {instance}, scrapeInterval: {scrapeInterval}", file = f)
        metrics = getmetrics.GetMetrics(prometheus_url, instance, job)
        for metric in metrics.get_metrics_for_instance():
            print(metric, file = f)
    f.close()

if __name__ == "__main__":
    prometheus_url = sys.argv[1]
    main(prometheus_url)
