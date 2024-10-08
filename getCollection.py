#!/usr/bin/env python3

import getinstances
import getmetrics


prometheus_url = "http://172.16.10.208:9091"
instances = getinstances.GetInstances(prometheus_url)
for job, instance, scrapeInterval in instances.get_prometheus_instances():
    print(f"Job: {job}, Instance: {instance}, scrapeInterval: {scrapeInterval}")
    metrics = getmetrics.GetMetrics(prometheus_url, instance, job)
    for metric in metrics.get_metrics_for_instance():
        print(metric)
