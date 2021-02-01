def test_job_metric():
    from shopcloud_metric import JobMetric

    job = JobMetric('sage-supplier-update', 
        instance='airflow-production', 
        env='testing',
    )
    with job as j:
        j.gauge('job_last_success_unixtime', labels={'supplier': 'EP'})
    