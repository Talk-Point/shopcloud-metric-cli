import os

def test_job_metric():
    os.environ["SECRETHUB_TOKEN"] = "123456"
    
    from shopcloud_metric import JobMetric

    job = JobMetric('sage-supplier-update', 
        instance='airflow-production', 
        env='testing',
    )
    with job as j:
        j.gauge('job_last_success_unixtime', labels={'supplier': 'EP'})
