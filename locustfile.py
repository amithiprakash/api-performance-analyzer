from locust import HttpUser, task, between
class APIUser(HttpUser):
    wait_time=between(1,2)
    @task
    def test_api(self):
        self.client.get("https://jsonplaceholder.typicode.com/posts")


