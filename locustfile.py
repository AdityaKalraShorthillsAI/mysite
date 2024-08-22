import random
from locust import HttpUser, task, between, TaskSet
 
class DemographicDataTasks(TaskSet):
    wait_time = between(1, 5)  # wait time between tasks in seconds
 
    @task(1)
    def get_demographicdata(self):
        pk = random.randint(1, 50000)
        self.client.get(f"crudx10m/demographicdata/{pk}/")
 
    # @task(1)
    # def post_demographicdata(self):
    #     data = {
    #         "age": random.randint(18, 90),
    #         "workclass": random.randint(1, 2000),
    #         "fnlwgt": random.randint(10000, 99999),
    #         "education": random.randint(1, 2000),
    #         "education_num": random.randint(1, 16),
    #         "marital_status": random.randint(1, 7),
    #         "occupation": random.randint(1, 14),
    #         "relationship": random.randint(1, 6),
    #         "race": random.randint(1, 5),
    #         "sex": random.randint(1, 2),
    #         "native_country": random.randint(1, 40),
    #         "capital_gain": random.randint(0, 10000),
    #         "capital_loss": random.randint(0, 10000),
    #         "hours_per_week": random.randint(1, 60)
    #     }
    #     self.client.post("crudx10m/demographicdata/", json=data)
 
    # @task(1)
    # def put_demographicdata(self):
    #     pk = random.randint(2120001, 2200000)
    #     data = {
    #         "age": random.randint(18, 90),
    #         "workclass": random.randint(1, 2000),
    #         "fnlwgt": random.randint(10000, 99999),
    #         "education": random.randint(1, 2500),
    #         "education_num": random.randint(1, 16),
    #         "marital_status": random.randint(1, 7),
    #         "occupation": random.randint(1, 14),
    #         "relationship": random.randint(1, 6),
    #         "race": random.randint(1, 5),
    #         "sex": random.randint(1, 2),
    #         "native_country": random.randint(1, 40),
    #         "capital_gain": random.randint(0, 10000),
    #         "capital_loss": random.randint(0, 10000),
    #         "hours_per_week": random.randint(1, 60)
    #     }
    #     self.client.put(f"crudx10m/demographicdata/{pk}/", json=data)
 
 
 
class WebsiteUser(HttpUser):
    tasks = [DemographicDataTasks]
    wait_time = between(1, 5)