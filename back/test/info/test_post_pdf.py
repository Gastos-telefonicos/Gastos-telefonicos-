from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.phones import PhonesRepository, Phone
from src.domain.phones_and_cost import PhonesAndCostRepository


def test_should_return_phones_projects_and_costs():
    phone_repository = PhonesAndCostRepository(temp_file())
    app = create_app(repositories={"phones_cost": phone_repository})
    client = app.test_client()

    body = {
        "pdf": "JVBERi0xLjQKJfbk/N8KMSAwIG9iago8PAovVHlwZSAvQ2F0YWxvZwovVmVyc2lvbiAvMS40Ci9QYWdlcyAyIDAgUgo+PgplbmRvYmoKMiAwIG9iago8PAovVHlwZSAvUGFnZXMKL0tpZHMgWzMgMCBSXQovQ291bnQgMQo+PgplbmRvYmoKMyAwIG9iago8PAovVHlwZSAvUGFnZQovTWVkaWFCb3ggWzAuMCAwLjAgNjEyLjAgNzkyLjBdCi9QYXJlbnQgMiAwIFIKL0NvbnRlbnRzIDQgMCBSCi9SZXNvdXJjZXMgNSAwIFIKPj4KZW5kb2JqCjQgMCBvYmoKPDwKL0xlbmd0aCA4MgovRmlsdGVyIC9GbGF0ZURlY29kZQo+PgpzdHJlYW0NCnic03czVDA0UAhJ43IK4TIxUDA3M9EzNLZQCEnhMlDQNTSCcTTMTcwVTEwtFAwMDDUVQrJQZW2MzYycjQ2NjY2NjI2MDCwM7EBKXEO4AI4JEyMNCmVuZHN0cmVhbQplbmRvYmoKNSAwIG9iago8PAovRm9udCA2IDAgUgo+PgplbmRvYmoKNiAwIG9iago8PAovRjEgNyAwIFIKPj4KZW5kb2JqCjcgMCBvYmoKPDwKL1R5cGUgL0ZvbnQKL1N1YnR5cGUgL1R5cGUxCi9CYXNlRm9udCAvSGVsdmV0aWNhCi9FbmNvZGluZyAvV2luQW5zaUVuY29kaW5nCj4+CmVuZG9iagp4cmVmCjAgOAowMDAwMDAwMDAwIDY1NTM1IGYNCjAwMDAwMDAwMTUgMDAwMDAgbg0KMDAwMDAwMDA3OCAwMDAwMCBuDQowMDAwMDAwMTM1IDAwMDAwIG4NCjAwMDAwMDAyNDcgMDAwMDAgbg0KMDAwMDAwMDQwMiAwMDAwMCBuDQowMDAwMDAwNDM1IDAwMDAwIG4NCjAwMDAwMDA0NjYgMDAwMDAgbg0KdHJhaWxlcgo8PAovUm9vdCAxIDAgUgovSUQgWzxFMEZBRjBFMUI3NzcxOTgxRDQ5N0ZFMkZDQzcxNjFDNj4gPEUwRkFGMEUxQjc3NzE5ODFENDk3RkUyRkNDNzE2MUM2Pl0KL1NpemUgOAo+PgpzdGFydHhyZWYKNTYzCiUlRU9GCg=="
    }
    response = client.post("/api/docs", json=body, content_type="application/json")

    assert response.status_code == 200
    assert response.json == [{"phone": "747 458 001", "cost": "6,1322"}]
