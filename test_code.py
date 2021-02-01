import os

os.environ["SECRETHUB_TOKEN"] = "123456"

def test_job_metric_with():
    from shopcloud_metric import JobMetric

    job = JobMetric('sage-supplier-update', 
        instance='airflow-production', 
        env='testing',
    )
    with job as j:
        j.gauge('job_last_success_unixtime', labels={'supplier': 'EP'})
    
    job.success()


def test_job_metric_success():
    from shopcloud_metric import JobMetric

    job = JobMetric('sage-supplier-update', 
        instance='airflow-production', 
        env='testing',
    )
    job.gauge('job_last_success_unixtime', labels={'supplier': 'EP'})
    job.success()


def test_job_metric_failed():
    from shopcloud_metric import JobMetric

    job = JobMetric('sage-supplier-update', 
        instance='airflow-production', 
        env='testing',
    )
    job.gauge('job_last_success_unixtime', labels={'supplier': 'EP'})
    job.failed()
